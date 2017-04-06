from lback.backup import Backup
from lback.utils import lback_backup, lback_backup_file_chunks, lback_backup_remove
import agent_pb2
import agent_pb2_grpc
from itertools import tee

class Agent(agent_pb2_grpc.AgentServicer):
  def DoBackup(self, request_iterator, context):    
    iter_copy = tee( request_iterator )
    request = iter_copy()
    db_backup = lback_backup( request.id )
    backup = Backup( request_cmd.id, db_backup['folder'] )
    def backup_chunked_iterator():
    	for backup_cmd_chunk in request_iterator():
	     set_backup_if_needed( backup_cmd_chunk )
	     yield backup_cmd_chunk.raw_data
    try:
	backup.run_chunked( backup_chunked_iterator )
    except Exception,ex:
	return agent_pb2.BackupCmdStatus( errored=True )
    return agent_pb2.BackupCmdStatus( errored=False )

  def DoMvTake(self, request, context):
     try:
	for file_chunk_res in lback_backup_file_chunks( request.id ):
	    yield agent_pb2.MvCmdGiveStatus( raw_data=file_chunk_res, errored=False)
     except Exception,ex:
         return agent_pb2.MvCmdGiveStatus( errored=True )
  def DoMvGive(self, request_iterator, context):
    iter_copy = tee( request_iterator )
    request = iter_copy()
    db_backup =lback_backup( request.id )
    backup = Backup( request.id, db_backup['folder'] )
    def mv_cmd_chunked_iterator():
	 for mv_cmd_chunk in request_iterator():
	      yield mv_cmd_chunk.raw_data
    try:
        for mv_chunk_res in backup.run_chunked( mv_chunked_iterator ):
	    yield agent_pb2.MvCmdStatus(errored=False)
    except Exception,ex:
	 return agent_pb2.MvCmdStatus(errored=True )

  def DoRestore(self, request, context):
    db_backup =lback_backup( request.id )
    restore = Restore( request.id, folder=db_backup['folder'] )
    try:
         for restore_file_chunk in restore.read_chunked():
	     yield agent_pb2.RestoreCmdStatus( 
		errored=False,
		raw_data=restore_file_chunk )
    except Exception,ex:
	return agent_pb2.RestoreCmdStatus( errored=True )

  def DoRm(self, request, context):
    try:
       lback_backup_remove( request.id )
       return agent_pb2.RmCmdStatus( errored=False )
    except Exception,ex:
       return agent_pb2.RmCmdStatus( errored=True )
