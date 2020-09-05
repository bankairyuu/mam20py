Feature: Connecting to the arduino device
  As the application starts, the serial I/O port chooser appears
  The users must choose the Arduino device from the list to connect.

  Scenario: Connect to the Arduino
    When the user choose the io port
    Then the remote controller tries to connect