from lback.backup import Backup
from lback.utils import lback_backup, lback_backup_chunked_file, lback_backup_remove, lback_output
from lback.restore import Restore
from . import agent_pb2
from . import agent_pb2_grpc
from . import shared_pb2
from . import shared_pb2_grpc
from itertools import tee
from traceback import print_exc

class Agent(agent_pb2_grpc.AgentServicer):
  def DoBackup(self, request_iterator, context):    
    lback_output("Received COMMAND DoBackup")
    request_iterator, iter_copy= tee( request_iterator )
    request = next(iter_copy)
    db_backup = lback_backup( request.id )
    lback_output("Running backup on %s"%( request.id ))
    backup = Backup( request.id, db_backup.folder )
    def backup_chunked_iterator():
    	for backup_cmd_chunk in request_iterator:
	     yield backup_cmd_chunk.raw_data
    try:
	backup.write_chunked( backup_chunked_iterator() )
    except Exception,ex:
	print_exc(ex)
	return shared_pb2.BackupCmdStatus( errored=True )
    lback_output("BACKUP COMPLETE")
    return shared_pb2.BackupCmdStatus( errored=False )

  def DoRelocateTake(self, request, context):
     lback_output("Received COMMAND DoRelocateTake")
     try:
        iterator = lback_backup_file_chunks( request.id )
	for file_chunk_res in iterator:
    	    lback_output("PACKING RELOCATE BACKUP CHUNK")
	    yield shared_pb2.RelocateCmdGiveStatus( raw_data=file_chunk_res, errored=False)
     except Exception,ex:
         yield shared_pb2.RelocateCmdGiveStatus( errored=True )
  def DoRelocateGive(self, request_iterator, context):
    lback_output("Received COMMAND DoRelocateGive")
    request_iterator, iter_copy = tee( request_iterator )
    request = next(iter_copy)
    db_backup =lback_backup( request.id )
    backup = Backup( request.id, db_backup.folder )
    def relocate_cmd_chunked_iterator():
	 for relocate_cmd_chunk in request_iterator:
    	      lback_output("SAVING RELOCATE BACKUP GIVE CHUNK")
	      yield relocate_cmd_chunk.raw_data
    try:
	iterator = backup.run_chunked( relocate_chunked_iterator )
        for relocate_chunk_res in iterator:
	    yield shared_pb2.RelocateCmdStatus(errored=False)
    except Exception,ex:
	 print_exc(ex)
	 yield shared_pb2.RelocateCmdStatus(errored=True )

  def DoRestore(self, request, context):
    lback_output("Received COMMAND DoRestore")
    db_backup =lback_backup( request.id )
    restore = Restore( request.id, folder=db_backup.folder )
    try:
	 iterator = restore.read_chunked()
         for restore_file_chunk in iterator:
    	     lback_output("PACKING RESTORE CHUNK")
	     yield shared_pb2.RestoreCmdStatus( 
		errored=False,
		raw_data=restore_file_chunk )
    except Exception,ex:
	print_exc(ex)
	yield shared_pb2.RestoreCmdStatus( errored=True )

  def DoRm(self, request, context):
    lback_output("Received COMMAND DoRm")
    try:
       lback_backup_remove( request.id )
    except Exception,ex:
       print_exc(ex)
       return shared_pb2.RmCmdStatus( errored=True )
    lback_output("REMOVE COMPLETE")
    return shared_pb2.RmCmdStatus( errored=False )
