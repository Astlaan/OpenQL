/**
 * @file   openql.h
 * @date   11/2016
 * @author Nader Khammassi
 * @brief  main openql header
 */
#ifndef OPENQL_H
#define OPENQL_H

#include "instruction_map.h"
#include "optimizer.h"
#include "circuit.h"
#include "transmon.h"
#include "program.h"

#include <fstream>
#include <map>

namespace ql
{
/**
 * openql types
 */

typedef std::vector<float> sweep_points_t;
typedef std::stringstream  str_t;


/**
 * configurable instruction map
 */
/* static */ dep_instruction_map_t dep_instruction_map;
/* static */ // bool              initialized = false;
/* static */ // ql_platform_t     target_platform;

// target platform
ql::quantum_platform           target_platform;          


// deprecated : for back compatibility
// should be removed
/*
void init(ql_platform_t platform, std::string dep_instruction_map_file="")
{
}
*/

void set_platform(ql::quantum_platform platform)
{
    target_platform = platform;
}


/**
 * generate qasm for a give circuit
 */
std::string qasm(ql::circuit c)
{
    std::stringstream ss;
    for (size_t i=0; i<c.size(); ++i)
    {
        ss << c[i]->qasm() << "\n";
        // COUT(c[i]->qasm());
    }
    return ss.str();
}

}

#endif // OPENQL_H