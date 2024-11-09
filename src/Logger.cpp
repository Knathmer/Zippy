#include "../include/Logger.h"
#include <fstream>
#include <iostream>
#include <ctime>
/*
This file is in charge of logging.
When initialized it needs to be given the path of where logs need to go.
*/
Logger::Logger(const std::string& logFilePath) : logFilePath(logFilePath) {}

void Logger::log(const std::string& message){
    
    std::ofstream logFile(this->logFilePath, std::ios_base::app); //Second argument means just add more to whatever already exists
    if(!logFile){
        std::cerr << "Could not open log file: " << logFilePath << "\n";
        return;
    }
    std::time_t now = std::time(nullptr);
    logFile << std::ctime(&now) << ": " << message << "\n";
}
