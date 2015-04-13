
class LoadBalancer(object):

    def __init__(self):
        self.priority = 0
        self.load = 0

    def set_priority(self, priority):
        self.priority = priority

    def set_load(self, load):
        self.load = load

    def print_details(self):
        print "Priority: %f" % self.priority
        print "Load: %f" % self.load

if __name__ == '__main__':
    print "Enter number of servers:"
    number_of_servers = int(raw_input())

    servers = []
    for i in range(number_of_servers):
        s = LoadBalancer()
        print "Server %d" % (i + 1)
        print "-----------"
        print "Priority: "
        s.set_priority(float(raw_input()))
        servers.append(s)
        print "----------------------------"
        print

    print "Enter load: "
    load = float(raw_input())
    temp_load = load

    new_servers = sorted(servers, key=lambda x: x.priority, reverse=True)

    for i in range(len(new_servers)):
        new_servers[i].set_load(load * new_servers[i].priority / 100)
        temp_load -= new_servers[i].load
        if temp_load < 0:
            break

    for i in range(len(new_servers)):
        print "Server %d" % (i + 1)
        print "-----------"
        new_servers[i].print_details()
        print "----------------------------"
        print

