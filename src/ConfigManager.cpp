#include "../include/ConfigManager.h"
#include <fstream>
#include <string>
#include <iostream>
#include "../include/nlohmann/json.hpp"
/*
This file is in charge of getting the config information regarding extraction path
Wherever this is initialized, it needs to be given the path for the configData.
*/

using json = nlohmann::json; //json is the alias

ConfigManager::ConfigManager(const std::string& configPath): configPath(configPath) {}

std::string ConfigManager::getExtractionPath() const{
    return extractionPath;
}
void ConfigManager::setExtractionPath(const std::string& newPath){
    this->extractionPath = newPath;
}
bool ConfigManager::loadConfig(){
    std::ifstream configFile(configPath);
    if(!configFile){
        std::cerr << "Could not open the config file: " << configPath << "\n";
        return false;
    }
    json configData;
    configFile >> configData; //Configdata parses the json data
    this->extractionPath = configData.value("extraction_path","C:\\ExtractedFiles"); //First is tag, second is default if no value
    return true;
}
bool ConfigManager::saveConfig(){ //Writes extraction path to the json file
    std::ofstream configFile(configPath); //Opens the config json
    if(!configFile){
        std::cerr << "Could not open the config file to write: " << configPath << "\n";
        return false;
    }
    json configData; //Create a json
    configData["extraction_path"] = this->extractionPath; //Create a key-value pair for the above json

    configFile << configData.dump(4); // WRite that to the configFile
    return true;
}