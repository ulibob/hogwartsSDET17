


class App:
    def start(self):

        return self
        pass

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        self.driver.stop_app()

