#ifndef CONFIG_MANAGER_H //Prevents defining more than once
#define CONFIG_MANAGER_H

#include <string>

class ConfigManager {

public:
    ConfigManager(const std::string& configPath);
    std::string getExtractionPath() const;
    void setExtractionPath(const std::string& newPath);    
    bool loadConfig();
    bool saveConfig();

private:
    std::string configPath;
    std::string extractionPath;

};

#endif