/**
 * @file   circuit.h
 * @date   11/2016
 * @author Nader Khammassi
 * @brief  gate container implementation
 */

#ifndef CIRCUIT_H
#define CIRCUIT_H

#include <vector>
#include <iostream>

#include "gate.h"

#define __print_circuit__ 0

namespace ql
{

   typedef std::vector<gate*> circuit;


   void print(circuit& c)
   {
      std::cout << "-------------------" << std::endl;
      for (size_t i=0; i<c.size(); i++)
      {
         std::cout << "   " << c[i]->qasm() << "(" << __print_gate_type(c[i]->type()) <<  ")" << std::endl;
      }
      std::cout << "\n-------------------" << std::endl;
   }
}

#endif // CIRCUIT_H
