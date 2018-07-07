#include <Arduino.h>
#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

void setup() {
    /* Fixes the output frequency (2Hz) and activates the ports.*/
    Serial.begin(115200);
    GPS.begin(9600);
    GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
    GPS.sendCommand(PMTK_SET_NMEA_INPUT_2HZ);
    GPS.sendCommand(PGCMD_ANTENNA);
}

void loop() {
    /* Parses the NMEA and confirms it.*/
    GPS.parse(GPS.lastNMEA());
    GPS.newNMEAreceived();

    /* Updates the fix and quality.*/
    Serial.print("Fix: ");
    Serial.println((int)GPS.fix);
    Serial.print("Quality: ");
    Serial.println((int)GPS.fixquality);

    /* Updates the time.*/
    Serial.print("Time: ");
    Serial.print(GPS.hour, DEC); Serial.print(":");
    Serial.print(GPS.minute, DEC); Serial.print(":");
    Serial.print(GPS.second, DEC); Serial.print(":");
    Serial.println(GPS.milliseconds);

    /* Updates the date.*/
    Serial.print("Date: ");
    Serial.print(GPS.year, DEC); Serial.print("/");
    Serial.print(GPS.month, DEC); Serial.print("/20");
    Serial.println(GPS.day, DEC);

    /* Updates the location, and altitude.*/
    Serial.println("Location: ");
    Serial.print("Latitude: ");
    Serial.print(GPS.latitude,3); Serial.print(" ");
    Serial.print("Longitude: ");
    Serial.println(GPS.longitude,3);
    Serial.println("Location Degrees: ");
    Serial.print("Latitude Degrees: ");
    Serial.print(GPS.latitudeDegrees,4); Serial.print(" ");
    Serial.print("Longitude Degrees: ");
    Serial.println(GPS.longitudeDegrees,4);
    Serial.print("Elevation: ")
    Serial.println(GPS.altitude);

    /* Updates the speed and direciton of motion.*/
    Serial.println("Rover Motion: ");
    Serial.print("Speed: ");
    Serial.println(GPS.speed);
    Serial.print("Angle: ");
    Serial.println(GPS.angle);

    Serial.println("Satellites on Rover: %d", (int)GPS.satellite));
}
