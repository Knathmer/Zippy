#ifndef LOGGER_H
#define LOGGER_H

#include <string>

class Logger {
public:
    Logger(const std::string& logFilePath);
    void log(const std::string& message);

private:
    std::string logFilePath;
};

#endif