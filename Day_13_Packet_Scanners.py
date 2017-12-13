
class firewall_class(object):
    def __init__(self, firewall):
        self.firewall_info = firewall
        self.num_layers = 0
        self.package_position = -1
        self.initial_position = 1
        self.layers = dict()
        self.move_forward = True
        self.is_caught = True
        self.severity = -1
        self.read_firewall()

    def reset_firewall(self):
        self.package_position = -1
        self.is_caught = False
        self.severity = -1
        self.layers_tmp = dict(self.layers)

    def add_delay(self):
        self.increase_step_scanner(True)
        self.severity = 0

    def read_firewall(self):
        for layer_info in self.firewall_info:
            id_layer = layer_info.split(':')[0]
            range_layer = int(layer_info.split(':')[1])
            self.layers.update({id_layer : [range_layer, self.initial_position, self.move_forward]})
        self.layers_tmp = dict(self.layers)
        self.num_layers = int(id_layer)

    def increase_step_package(self):
        self.package_position+=1

    def move_one_step_scanner(self, layer):
        if layer[0] == layer[1]:
            return [layer[0], layer[1] - 1, False]
        elif layer[1] == 1:
            return [layer[0], layer[1] + 1, True]
        elif layer[2]:
            return [layer[0], layer[1] + 1, layer[2]]
        else:
            return [layer[0], layer[1] - 1, layer[2]]

    def increase_step_scanner(self, is_original_pos = False):
        if is_original_pos:
            self.layers.update((x, self.move_one_step_scanner(y)) for x, y in self.layers.items())
        else:
            self.layers_tmp.update((x, self.move_one_step_scanner(y)) for x, y in self.layers_tmp.items())

    def check_if_caught(self):
        element = self.layers_tmp.get(str(self.package_position))
        if not element == None and int(element[1]) == 1:
            self.severity += element[0]*self.package_position
            self.is_caught = True

    def get_severity(self):
        return self.severity

    def get_caught(self):
        return self.is_caught


def run_Packet_Scanners_1(firewall):

    for _ in xrange(firewall.num_layers+1):
        firewall.increase_step_package()
        firewall.check_if_caught()
        firewall.increase_step_scanner()

    print 'The solution is ' + str(firewall.get_severity())


def run_Packet_Scanners_2(firewall):

    delay = -1
    while(firewall.get_caught()):

        delay += 1
        firewall.reset_firewall()

        for _ in xrange(firewall.num_layers + 1):

            firewall.increase_step_package()
            firewall.check_if_caught()
            firewall.increase_step_scanner()

            if firewall.get_severity() > 0 or firewall.get_caught():
                break

        firewall.add_delay()

    print 'The solution is ' + str(delay)


def open_file_txt(file_name):
    file = open(file_name, 'r')
    return [line[0:len(line)].replace("\n", "") for line in file.readlines()]


if __name__ == '__main__':
    firewall_file = open_file_txt('./file_directory/Day_13.txt')

    run_Packet_Scanners_1(firewall_class(firewall_file))
    run_Packet_Scanners_2(firewall_class(firewall_file))
