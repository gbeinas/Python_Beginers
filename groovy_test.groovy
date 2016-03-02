#!/usr/bin/bash

def LOCAL = "git rev-parse master"
def REMOTE = "git rev-parse origin/master"
def BASE = "git merge-base master origin/master"


def local_exec = LOCAL.execute();
def loc_exec_outputStream = new StringBuffer();
local_exec.waitForProcessOutput(loc_exec_outputStream, System.err);

def remote_exec = REMOTE.execute();
def rem_exec_outputStream = new StringBuffer();
remote_exec.waitForProcessOutput(rem_exec_outputStream, System.err);

def base_exec = BASE.execute();
def base_exec_outputStream = new StringBuffer();
base_exec.waitForProcessOutput(base_exec_outputStream, System.err);

/*print "The local ref is : " + local_exec.text
print "The remote ref is : " + remote_exec.text
print "The base ref is :  " + base_exec.text*/

print "The local ref is : " + loc_exec_outputStream.toString()
print "The remote ref is : " + rem_exec_outputStream.toString()
print "The base ref is :  " + base_exec_outputStream.toString()

if(loc_exec_outputStream.toString()==rem_exec_outputStream.toString()){
	System.out.println("Up-to-date");
	System.out.println("Script run with success");
}
else if(loc_exec_outputStream.toString() == base_exec_outputStream.toString()){
	System.out.println("Need to pull");
	System.out.println("Script run with success");
}
else if(rem_exec_outputStream.toString() == base_exec_outputStream.toString()){
	System.out.println("Need to push");
	System.out.println("Script run with success");
}

