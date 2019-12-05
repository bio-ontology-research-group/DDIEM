#!/bin/python3;
a="""



This script will trickle down the value of each non empty field to all the contigous empty cells beneath it. 

pushd .;cd /local/data/development.minor/KAUST/BORG/try1;

#export src_csv_dataset_file_name="../raw_data/2019-10-01/BORG_DDIEM__clinical_logs.2019-10-01.1418hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-10-10/BORG_DDIEM__clinical_logs.2019-10-10.0958hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-10-16/BORG_DDIEM__clinical_logs.2019-10-16.0900hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-10-27/BORG_DDIEM__clinical_logs.2019-10-27.1048hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-10-31/BORG_DDIEM__clinical_logs.2019-10-31.1014hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-11-22/BORG_DDIEM__clinical_logs.2019-11-22.0032hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-12-03/BORG_DDIEM__clinical_logs.2019-12-03.1025hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-12-03/BORG_DDIEM__clinical_logs.2019-12-03.1140hrs.csv";
#export src_csv_dataset_file_name="../raw_data/2019-12-04/BORG_DDIEM__clinical_logs.2019-12-04.0804hrs.csv";
export src_csv_dataset_file_name="../raw_data/2019-12-05/BORG_DDIEM__clinical_logs.2019-12-05.0910hrs.csv";


working_dir_file_name="/local/data/tmp/BORG_DDIEM/BORG_DDIEM__parse_clinical_logs_CSV.working_dir" \
 && count_of_workers=1 \
 && log_file_name="/local/data/tmp/BORG_DDIEM/logs/BORG_DDIEM__dataset.csv.log.`date +%Y-%m-%d.%H%M.%S.%N.%Z`" \
 && echo `date +%Y-%m-%d.%H%M.%S.%N.%Z`", log_file_name is:'${log_file_name}'" \
 && mkdir -p "$(dirname ${log_file_name})" \
 && pushd . && cd /local/data/development.minor/KAUST/BORG/try1 \
 && PYTHON_HOME="/local/data/apps/python/3.8.0" \
 && date && time "${PYTHON_HOME}"/bin/python3 src/py/clinical_logs_data_transformation/amqp/BORG_DDIEM__parse_clinical_logs_CSV.py \
 -f"${src_csv_dataset_file_name}" \
 -d"/local/data/development.minor/KAUST/BORG/raw_data" \
 --count_of_workers=${count_of_workers} \
 2>&1|tee "${log_file_name}" \
 && popd && date;
 
rm -rf /local/data/development.minor/KAUST/BORG/raw_data/2019-*/.~lock.*

""";

#from xml.sax import saxutils;
#import xml.sax;

import sys;
import os;
import getopt;
from optparse import OptionParser;
import errno;
import csv;
import re;
import time;
import json;
import logging;
import errno;
import sys, traceback;
import datetime;
import socket;
import multiprocessing;






LOG_FORMAT=('%(levelname) -5s processes_id:%(process)d time:%(asctime)s %(name) -10s [%(pathname)s %(module)s %(funcName) '
    '-15s %(lineno) -5d]: %(message)s');
LOGGER = logging.getLogger(__name__);

def run_BORG_DDIEM__parse_clinical_logs_CSV(
    w
    ,queue
    ,worker_id
):
    try:
        w.run();
        queue.put(w._processing_outcome__dict);
    except KeyboardInterrupt:
        d.stop();
class BORG_DDIEM__parse_clinical_logs_CSV():
    def __init__(
        self
        ,hostname,ipAddress,ppid
        ,task_id
        ,task_formulation_timestamp
        ,worker_id
        ,worker_number
        ,working_dir_file_name
        ,_srcCSVFileName
        ,_destCSVDirFileName
    ):
        doc="""
        an object if this class performs the tranformation of XML to JSON.
        """;
        self.LOG_FORMAT=('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
            '-35s %(lineno) -5d: %(message)s');
        self.logging_level__value="INFO";
        
        self.working_dir_file_name=working_dir_file_name;
        self.hostname=hostname;
        self.ipAddress=ipAddress;
        self.ppid=os.getppid();
        self.pid=os.getpid();
        self.task_formulation_timestamp=task_formulation_timestamp;
        self.task_id=task_id;
        self.worker_id=worker_id;
        self.worker_number=worker_number;
        self._srcCSVFileName=_srcCSVFileName;
        self._destCSVDirFileName=_destCSVDirFileName;
        self._processing_outcome__dict=None;
        
        try:
            if(_srcCSVFileName==None or len(_srcCSVFileName.strip())<0):
                pass;
                raise ValueError("_srcCSVFileName is empty the supplied value is '%s'"%(_srcCSVFileName));
        except ValueError as error:
            #see "/local/data/BCL_FE_ABI3730_sequencer_plate_data_generator_jobs_data/2018/2018-09/2018-09-20/2018-09-20_171025_103.processing_outcome.json"
            #LOGGER.info(" '%s', -------------- cmd is:'%s', row_cnt is:%d"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),cmd,row_cnt));
            LOGGER.exception(error);
            LOGGER.exception(traceback.format_exc());
            
            raise error;
    def run(self):
        self._processing_outcome__dict=cascade_fields_values(
            self.hostname,self.ipAddress,self.ppid,self.pid
            ,self.working_dir_file_name
            ,self.task_id
            ,self.task_formulation_timestamp
            ,self.worker_id
            ,self.worker_number
            ,self._srcCSVFileName
            ,self._destCSVDirFileName
        );
        LOGGER.info("self._processing_outcome__dict is:'%s'"%(json.dumps(self._processing_outcome__dict,indent=4)));
    def get_processing_outcome(self):
        return self._processing_outcome__dict;

def cascade_fields_values(
    hostname,ipAddress,ppid,pid
    ,working_dir_file_name
    ,task_id
    ,task_formulation_timestamp
    ,worker_id
    ,worker_number
    ,_srcCSVFileName
    ,_destCSVDirFileName
):
    pass;
    processing_outcome__dict={};
    task_commencement_time_obj=datetime.datetime.now();
    task_commencement_time_str=task_commencement_time_obj.strftime('%Y-%m-%d %H:%M:%S.%f');
    
    """
1/Below are the trickle-down eligible fields, as provided by Dr. Marwa.
OMIM no. (field#3)
Disease name (field#4)
Gene affected (field#6)
Enzyme/ protein (field#7)
Drug name (field#9)
Drug ID (field#11)
References (fields#23 till field#33)




I am try to interdepencies between the various fields of the clinical logs dataset.
This information will help me know how to 



    """;
    trickle_down_eligible_field__list=[2,3,5,6,7,10,11,24,25,26,27,28,29,30,31,32];
    #trickle_down_eligible_field__list=[2,3,5,6,7,8,9,10,23,24,25,26,27,28,29,30,31];
    #trickle_down_eligible_field__list=[2,3,5,6,7,8,9,10,22,23,24,25,26,27,28,29,30,31,32];
    #trickle_down_eligible_field__list=[2,3,5,6,7];
    
    src_dataset_csv_file_name=_srcCSVFileName;
    dest_dataset_csv_file_name=os.path.join(
        _destCSVDirFileName
        ,os.path.basename(os.path.dirname(_srcCSVFileName))
        ,"%s.collapsed.csv"%(os.path.splitext(os.path.basename(_srcCSVFileName))[0])
    );
    LOGGER.info("dest_dataset_csv_file_name is:'%s'"%(dest_dataset_csv_file_name));
    mkdir_p(os.path.dirname(os.path.abspath(dest_dataset_csv_file_name)));
    
    src_dataset_csv_fh=None;
    src_dataset_csv_reader=None;
    src_dataset_csv_fh=open(src_dataset_csv_file_name,"r");
    src_dataset_csv_reader=csv.reader(
        src_dataset_csv_fh
        ,delimiter=","
        ,quotechar='"'
        ,quoting=csv.QUOTE_MINIMAL
    );
    
    dest_dataset_csv_fh=None;
    dest_dataset_csv_writer=None;
    dest_dataset_csv_fh=open(dest_dataset_csv_file_name,"w");
    dest_dataset_csv_writer=csv.writer(dest_dataset_csv_fh,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL);
    
    drug_ID__previous="";
    cnt_of_fields__max=0;
    populated_fields__dict={};
    row2=[];
    cnt_of_fields=0;
    row_cnt=0;
    src_dataset_csv_fh.seek(0);
    drug_name=None;
    for row in src_dataset_csv_reader:
        row_cnt+=1;
        del row2[:];
        if(1==1 or row_cnt<5):
            """
            Here we test to see if the drug value in the new row matches that of the preceeding row.
            If it does not match we reset the stored values of the fields right of it. 
            """
            omim_ID=row[2].strip();
            drug_ID=row[11].strip();
            #LOGGER.info("--------------------------------------------------------------------------drug_ID is '%s'"%(drug_ID));
            if(len(omim_ID.strip())>0 or len(drug_ID.strip())>0):
                #if(int(row[0])>88 and int(row[0])<94):
                #LOGGER.info("---------------------------------------------------------row[0] is:{0}, drug_ID is '{1}'".format(row[0],drug_ID));
                pass;
                for i in range(11,34+1):
                    pass;
                    populated_fields__dict[i]=None;#
            if(drug_ID==drug_ID__previous):
                pass;
                for i in range(11,34+1):
                    pass;
                    #populated_fields__dict[i]=None;#
                
            """
            Here we test if the drug name field is non empty.
            If it is empty we reset the stored values of the fields to the right of it.
            """
            drug_name=row[10].strip();
            if(drug_name.upper()=="No treatment is available in DDIEM".upper()):
                pass;
                #drug_name="";
                for i in range(11,34+1):
                    pass;
                    populated_fields__dict[i]=None;
            elif(drug_name==""):
                for i in range(10,34+1):
                    pass;
                    #populated_fields__dict[i]=None;
                    
            for i, val in enumerate(row):
                row[i]=row[i].strip();
                """
                For each non-trickle-down-eligible-field clean out its previous value.
                """
                if(i in trickle_down_eligible_field__list):
                    pass;
                else:
                    populated_fields__dict[i]=None;
                """
                Test if the field is non-empty, if it is inject this value into the populated_fields__dict dictionary, use the field ordinal position as the key and the field value as the value.
                """
                if(len(row[i])>0):
                    """
                    Inject this value into the populated_fields__dict dictionary.
                    """
                    populated_fields__dict[i]=row[i];
                
            #LOGGER.info("row_cnt is:%d, row is:'%s', populated_fields__dict is:'%s'"%(row_cnt,json.dumps(row,indent=4),json.dumps(populated_fields__dict,indent=4)));
            if(1==1):
                cnt_of_fields=len(row);
                if(cnt_of_fields__max<cnt_of_fields):
                    cnt_of_fields__max=cnt_of_fields;
                """
                Now loop through the dictionary using values from 0 till cnt_of_fields__max-1 as key.
                write out these values into an array which will be printed out to file.
                """
                i=0;
                while i<cnt_of_fields__max:
                    if(i in populated_fields__dict):
                        row2.append(populated_fields__dict[i]);
                    else:
                        row2.append("");
                    i+=1;
                """
                If the current row is the header row, reset the populated_fields__dict dictionary and obtain the values to write to the destination CSV from the row list.
                """
                if(row_cnt<=2):
                    row2=row[:];
                    """
                    These are header rows, let's reset the dictionary.
                    """
                    populated_fields__dict={};
                    
                dest_dataset_csv_writer.writerow(row2);
                drug_ID__previous=row2[11];
                del row2[0:len(row2)-1];
    dest_dataset_csv_fh.close();
    src_dataset_csv_fh.close();
    
    
    task_completion_time_obj=datetime.datetime.now();
    task_completion_time_str="%s"%(task_completion_time_obj.strftime('%Y-%m-%d %H:%M:%S.%f'));
    duration_obj=task_completion_time_obj-task_commencement_time_obj;
    duration_ms=duration_obj.total_seconds()*1000;
    
    processing_outcome__dict["task_commencement_time_str"]=task_commencement_time_str;
    processing_outcome__dict["task_completion_time_str"]=task_completion_time_str;
    processing_outcome__dict["duration_ms"]=duration_ms;
    
    processing_outcome__dict["hostname"]=hostname;
    processing_outcome__dict["ipAddress"]=ipAddress;
    processing_outcome__dict["ppid"]=ppid;
    processing_outcome__dict["pid"]=pid;
    processing_outcome__dict["task_id"]=task_id;
    processing_outcome__dict["task_formulation_timestamp_str"]=task_formulation_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f');
    processing_outcome__dict["worker_id"]=worker_id;
    processing_outcome__dict["worker_number"]=worker_number;
    processing_outcome__dict["src_dataset_csv_file_name"]=src_dataset_csv_file_name;
    processing_outcome__dict["dest_dataset_csv_file_name"]=dest_dataset_csv_file_name;
    processing_outcome__dict["cnt_of_fields__max"]=cnt_of_fields__max;
    
    return processing_outcome__dict;
    

    
def getLocalIPAddress():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
    s.connect(('google.com',80));
    return s.getsockname()[0];

def touch(file_name):
    mkdir_p(os.path.abspath(os.path.join(file_name, os.pardir)));
    with open(file_name,'a'):
        os.utime(file_name,None);

import errno;
def mkdir_p(path):
    if(not(os.path.exists(path) and os.path.isdir(path))):
        try:
            os.makedirs(path,exist_ok=True);
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise   


def format_my_nanos(nanos):
        dt = datetime.datetime.fromtimestamp(nanos / 1e9)
        #return '{}.{:09.0f}'.format(dt.strftime('%Y-%m-%dT%H:%M:%S'), nanos % 1e9);
        return '{}_{:09.0f}'.format(dt.strftime('%Y%m%d%H%M%S'), nanos % 1e9);


def timestamp_from_nano_seconds(nanos):
        dt = datetime.datetime.fromtimestamp(nanos / 1e9)
        #return '{}.{:09.0f}'.format(dt.strftime('%Y-%m-%dT%H:%M:%S'), nanos % 1e9);
        return '{}_{:09.0f}'.format(dt.strftime('%Y/%m/%d %H:%M:%S'), nanos % 1e9);


class InfiniteTimer():#see https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
    """A Timer class that does not stop, unless you want it to.""";
    def __init__(self, seconds, target, countdown__upperbound):
        self._should_continue = False;
        self.is_running = False;
        self.seconds = seconds;
        self.target = target;
        self.thread = None;
        self.countdown__upperbound=countdown__upperbound;
        
    def _handle_target(self):
        self.is_running = True;
        self.target();
        self.is_running = False;
        self._start_timer();
        
    def _start_timer(self):
        if self._should_continue: # Code could have been running when cancel was called.;
            self.thread = threading.Timer(self.seconds, self._handle_target);
            LOGGER.info("self.countdown__upperbound is:%d"%(self.countdown__upperbound));
            if(self.countdown__upperbound>0):
                self.thread.start();
                self.countdown__upperbound-=1;
            else:
                self._should_continue=False;
            
    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True;
            self._start_timer();
        else:
            print("Timer already started or running, please wait if you're restarting.");
            
    def cancel(self):
        if self.thread is not None:
            self._should_continue = False # Just in case thread is running and cancel fails.;
            self.thread.cancel();
        else:
            print("Timer never started or failed to initialize.");



from xml.sax import make_parser
from xml.sax.handler import feature_namespaces

if __name__ == '__main__':
    task_formulation_timestamp=None;#datetime.datetime.strptime('20180910_135822_123456', '%Y%m%d_%H%M%S_%f');
    task_formulation_timestamp_str=None;#'20180910_135822_123456';
    working_dir_file_name=None;
    src_csv_dataset_file_name=None;
    dest_csv_dataset_dir_name=None;
    count_of_workers=1;
    usage="usage: %prog [options] arg1 [[arg2]..]"
    version="version: 0.001"

    import argparse;
    parser=argparse.ArgumentParser();
    try:
        parser.add_argument("-t","--task_formulation_timestamp_str",action="append",type=str,dest="op__task_formulation_timestamp_str",help="""
            This variable will contain the current timestamp in 'Ymd_HMS_f' format, for example '20180910_135822_123456'. This timestamp will be the bases of the task id of this job.
        """);
        parser.add_argument("-o","--working_dir_file_name",action="append",type=str,dest="op__working_dir_file_name",help="""
            The full path to the directory where temporary data will be written.
        """);
        parser.add_argument("-f","--src_csv_dataset_file_name",action="append",type=str,dest="op__src_csv_dataset_file_name",help="The full path to the CSV file where the input dataset is to be found.")
        parser.add_argument("-d","--dest_csv_dataset_dir_name",action="append",type=str,dest="op__dest_csv_dataset_dir_name",help="The full directory path where the resultant CSV file will be written.")
        parser.add_argument("-w","--count_of_workers",action="append",type=int,dest="op__count_of_workers",help="""
            The count of workers to launch (via multiprocessing).
        """);
        
        (options)=parser.parse_args(sys.argv[1:])
        if len(sys.argv)<4:
            parser.error("""
                ERROR: Missing required arguments
                -t, --task_formulation_timestamp_str
                    This variable will contain the current timestamp in 'Ymd_HMS_f' format, for example '20180910_135822_123456'. This timestamp will be the bases of the task id of this job.
                -o, --working_dir_file_name
                    The full path to the directory where temporary data will be written.
                -f, --src_csv_dataset_file_name
                    The full path to the CSV file where the input dataset is to be found.
                -d, --dest_csv_dataset_dir_name
                    The full directory path where the resultant CSV file will be written.
                -w, --count_of_workers
                    The count of workers to launch (via multiprocessing).
            """);
            
        if(options.op__task_formulation_timestamp_str):
            task_formulation_timestamp_str=options.op__task_formulation_timestamp_str[0].strip();
        if(options.op__working_dir_file_name):
            working_dir_file_name=options.op__working_dir_file_name[0].strip();
        if(options.op__src_csv_dataset_file_name):
            src_csv_dataset_file_name=options.op__src_csv_dataset_file_name[0];
        if(options.op__dest_csv_dataset_dir_name):
            dest_csv_dataset_dir_name=options.op__dest_csv_dataset_dir_name[0];
            mkdir_p(os.path.abspath(os.path.join(dest_csv_dataset_dir_name, os.pardir)));
            mkdir_p(os.path.abspath(dest_csv_dataset_dir_name));
        if(options.op__count_of_workers):
            count_of_workers=int(options.op__count_of_workers[0]);

        #parser.destroy()
    except argparse.ArgumentError:
        #print help infor and exit
        usage()
        sys.exit(2)
    
    print("dest_csv_dataset_dir_name is:'%s'"%(dest_csv_dataset_dir_name));
    #print("dest_ddl_file_name is:'%s'"%(dest_ddl_file_name));
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT);
    
    task_formulation_timestamp=None;
    if(task_formulation_timestamp_str!=None and len(task_formulation_timestamp_str)>0):
        task_formulation_timestamp=datetime.datetime.strptime(task_formulation_timestamp_str, '%Y%m%d_%H%M%S_%f');
    else:
        task_formulation_timestamp=datetime.datetime.now();
    task_id="%s"%(task_formulation_timestamp.strftime('%Y-%m-%d_%H%M%S_%f')[:-3]);#import datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-1]
    
    hostname=socket.gethostname().strip();
    ipAddress=getLocalIPAddress();
    pid=os.getpid();
    worker_id='%s_%s_%d'%(hostname,ipAddress,pid);
    LOGGER.info(" '%s', -------------- hostname:'%s', ipAddress:'%s', pid:%d, worker_id:'%s', task_id:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),hostname,ipAddress,pid,worker_id,task_id));
    LOGGER.info(" '%s', -------------- src_csv_dataset_file_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),src_csv_dataset_file_name));
    LOGGER.info(" '%s', -------------- dest_csv_dataset_dir_name is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),dest_csv_dataset_dir_name));
    LOGGER.info(" '%s', -------------- count_of_workers is:'%s'"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),count_of_workers));
    process_list=[];
    queue_list=[];#this array will contain objects of multiprocessing.Queue (which is a near clone of queue.Queue)
    worker_list=[];
    
    try:
        for i in range(count_of_workers):
            #Instantiates the thread
            #(i) dos not make a sequence, so we use (i,)
            worker_id2='%s__%s__%d'%('BORG_DDIEM__parse_clinical_logs_CSV',worker_id,i);
            LOGGER.info(">>>>>>>>>>worker_tag:'%s'"%(worker_id2));
            
            worker_number=i;
            w=BORG_DDIEM__parse_clinical_logs_CSV(
                hostname,ipAddress,pid
                ,task_id
                ,task_formulation_timestamp
                ,worker_id2
                ,worker_number
                ,working_dir_file_name
                ,src_csv_dataset_file_name
                ,"%s"%(dest_csv_dataset_dir_name)
            );
            """
            t=threading.Thread(
                target=run_BORG_DDIEM__parse_clinical_logs_CSV
                ,args=(
                    d
                    ,worker_id2
                )
            );
            thread_list.append(t);
            worker_list.append(d);
            """
            q=multiprocessing.Queue();
            p=multiprocessing.Process(
                target=run_BORG_DDIEM__parse_clinical_logs_CSV
                ,args=(
                    w
                    ,q
                    ,worker_id2
                )
            );
            process_list.append(p);
            queue_list.append(q);
            worker_list.append(w);
            
        for process in process_list:
            process.start();
                
        #block the current process till join() returns
        #for process in process_list:
        for i,process in enumerate(process_list):
            cont=True;
            while(cont):
                #LOGGER.info("============Looping, i is:%d, process_list[%d].isAlive() is:'%s'"%(i,i,process_list[i].isAlive()));
                process.join(60);#wait for 60 seconds.
                if(process.is_alive()):
                    #timout occurred on process
                    cont=True;
                    #LOGGER.info("timeout occurred on process:'%s'."%(worker_list[i].worker_id));
                    #worker_list[i].stop();
                    #worker_list[i].some_function();
                else:
                    cont=False;
                    #LOGGER.info("execution completes for process:'%s'."%(worker_list[i].consumer_tag));
        for i,worker in enumerate(worker_list):
            pass;
            """
            """;
            #processing_outcome__dict=worker_list[i]._processing_outcome__dict;
            #processing_outcome__dict=worker_list[i].get_processing_outcome();
            processing_outcome__dict=queue_list[i].get();
            #LOGGER.info("[=]%s, %s"%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),json.dumps(processing_outcome__dict,indent=4)));
            LOGGER.info("processing_outcome__dict is:'%s'"%(json.dumps(processing_outcome__dict,indent=4)));
            worker_list[i]=None;
            worker=None;
            
    except KeyboardInterrupt:
        for i,worker in enumerate(worker_list):
            pass;
            """
            """;
            #cleanup
            #worker.cleanup();
            if(worker_list[i]!=None):
                worker_list[i].stop();
                processing_outcome__dict=worker_list[i]._processing_outcome__dict;
                worker_list[i]=None;
                worker=None;
        worker_list=None;
        queue_list=None;
        process_list=None;
    """
    except Exception as error:
        LOGGER.error("An error has been detected. Reason:'%s'"%(error));
        worker_list=None;
        thread_list=None;
    """
    worker_list=None;
    queue_list=None;
    process_list=None;

