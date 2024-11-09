#include "ConfigManager.h"
#include "Logger.h"
#include <iostream>

int main(){
    ConfigManager configManager("../config/app.config.json");
    std::cout << "Config poop" << std::endl;
    Logger logger("app.log");

    if (!configManager.loadConfig()) {
        logger.log("Failed to load config.");
        std::cerr << "Failed to load config.\n";
        return 1;
    }
    std::string extractionPath = configManager.getExtractionPath();
    std::cout << "Extraction path: " << extractionPath << "\n";
    logger.log("Loaded extraction path: " + extractionPath);
 
    // Example of updating config and saving it
    configManager.setExtractionPath("C:\\NewExtractedFiles");
    if (!configManager.saveConfig()) {
        logger.log("Failed to save config.");
        std::cerr << "Failed to save config.\n";
        return 1;
    }

    logger.log("Config saved successfully.");
    std::cout << "Config saved successfully.\n";

    return 0;
}