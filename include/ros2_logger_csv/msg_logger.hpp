#ifndef ros2_logger_csv_CPP_MSG_LOGGER_HPP
#define ros2_logger_csv_CPP_MSG_LOGGER_HPP

#include <fstream>
#include <sstream>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>


/**
 * 
 */
class Logger
{
public:
    explicit Logger(
        const std::string &log_file_path,
        bool overwrite = true
    );
    ~Logger();

    void log(
        const std::vector<std::string> &data
    );

private:
    std::ofstream log_file;     //
};


#endif // ros2_logger_csv_CPP_MSG_LOGGER_HPP
