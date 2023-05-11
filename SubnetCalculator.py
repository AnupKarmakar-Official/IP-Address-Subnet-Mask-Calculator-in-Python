import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox


class SubnetCalculator(QMainWindow):

    def __init__(self):
        super().__init__()

        # set window properties
        self.setWindowTitle("IP Address and Subnet Mask Calculator - v1.0")
        self.setGeometry(100, 100, 400, 300)

        # author label
        self.author_label = QLabel("Designed by Anup Karmakar (https://github.com/AnupKarmakar-Official)", self)
        self.author_label.setGeometry(20, 10, 400, 20)

        # create input fields
        self.ip_address_label = QLabel("IP Address:", self)
        self.ip_address_label.move(50, 50)

        # input fields
        self.ip_address_label = QLabel("IP Address:", self)
        self.ip_address_label.move(50, 50)

        # input fields
        self.ip_address_label = QLabel("IP Address:", self)
        self.ip_address_label.move(50, 50)

        self.ip_address_input = QLineEdit(self)
        self.ip_address_input.move(150, 50)
        self.ip_address_input.setPlaceholderText("Enter IP address...")

        self.subnet_mask_label = QLabel("Subnet Mask:", self)
        self.subnet_mask_label.move(50, 100)

        self.subnet_mask_input = QLineEdit(self)
        self.subnet_mask_input.move(150, 100)
        self.subnet_mask_input.setPlaceholderText("Enter subnet mask...")

        # buttons
        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.move(50, 150)
        self.calculate_button.clicked.connect(self.calculate)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.move(150, 150)
        self.clear_button.clicked.connect(self.clear)

        # output labels
        self.network_address_label = QLabel("Network Address:", self)
        self.network_address_label.move(50, 200)

        self.network_address_output = QLabel(self)
        self.network_address_output.move(150, 200)

        self.broadcast_address_label = QLabel("Broadcast Address:", self)
        self.broadcast_address_label.move(50, 225)

        self.broadcast_address_output = QLabel(self)
        self.broadcast_address_output.move(150, 225)

        self.hosts_label = QLabel("Number of Hosts:", self)
        self.hosts_label.move(50, 250)

        self.hosts_output = QLabel(self)
        self.hosts_output.move(150, 250)

    def calculate(self):
        # get input values
        ip_address = self.ip_address_input.text()
        subnet_mask = self.subnet_mask_input.text()

        # validate input values
        if not ip_address or not subnet_mask:
            QMessageBox.warning(self, "Error", "Please enter both IP address and subnet mask.")
            return

        ip_parts = ip_address.split(".")
        if len(ip_parts) != 4:
            QMessageBox.warning(self, "Error", "Invalid IP address format.")
            return

        subnet_parts = subnet_mask.split(".")
        if len(subnet_parts) != 4:
            QMessageBox.warning(self, "Error", "Invalid subnet mask format.")
            return

        # calculate the network and broadcast addresses
        network_address_parts = []
        broadcast_address_parts = []
        for i in range(4):
            network_address_parts.append(str(int(ip_parts[i]) & int(subnet_parts[i])))
            broadcast_address_parts.append(str(int(ip_parts[i]) | int(~int(subnet_parts[i]) & 0xff)))

        # calculate number of hosts
        num_zeros = str(bin(int(subnet_mask.replace(".", "")))).count("0")
        num_hosts = 2 ** num_zeros - 2

        # update output labels
        self.network_address_output.setText(".".join(network_address_parts))
        self.broadcast_address_output.setText(".".join(broadcast_address_parts))
        self.hosts_output.setText(str(num_hosts))

    def clear(self):
        # clear input and output fields
        self.ip_address_input.clear()
        self.subnet_mask_input.clear()
        self.network_address_output.clear


if __name__ == "__main__":
    # application
    app = QApplication(sys.argv)

    # main window
    window = SubnetCalculator()
    window.show()

    # run application
    sys.exit(app.exec_())
