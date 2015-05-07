import commands


def totalCoresUsed():
    return commands.getoutput("nova absolute-limits |grep totalCoresUsed |awk '{print $4}'") 

def totalInstancesUsed():
    return commands.getoutput("nova absolute-limits |grep totalInstancesUsed |awk '{print $4}'")

def totalRAMUserInGB():
    mem = commands.getoutput("nova absolute-limits |grep totalRAMUsed |awk '{print $4}'")
    mem = float(mem)
    mem = mem / 1024
    mem = round(mem, 1)
    return mem

def totalFloatingIpsUsed():
    return commands.getoutput("nova absolute-limits |grep totalFloatingIpsUsed |awk '{print $4}'")
def totalSecurityGroupsUsed():
    return commands.getoutput("nova absolute-limits |grep totalSecurityGroupsUsed |awk '{print $4}'")

def launchInstance():
    return commands.getoutput("fastnovaboot -n test -i Debian-7.7-server-amd64 -f m1.tiny -s ANTTIDEVEL_Digile_to_TriPort")

