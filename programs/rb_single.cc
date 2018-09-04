

#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <cassert>

#include <time.h>

#include <ql/openql.h>

// clifford inverse lookup table for grounded state
const size_t inv_clifford_lut_gs[] = {0, 2, 1, 3, 8, 10, 6, 11, 4, 9, 5, 7, 12, 16, 23, 21, 13, 17, 18, 19, 20, 15, 22, 14};
//const size_t inv_clifford_lut_es[] = {3, 8, 10, 0, 2, 1, 9, 5, 7, 6, 11, 4, 21, 13, 17, 12, 16, 23, 15, 22, 14, 18, 19, 20};

typedef std::vector<int> cliffords_t;


/**
 * build rb circuit
 */
void build_rb(int num_cliffords, ql::quantum_kernel& k)
{
   assert((num_cliffords%2) == 0);
   int n = num_cliffords/2;

   cliffords_t cl;
   cliffords_t inv_cl;

   // add the clifford and its reverse
   for (int i=0; i<n; ++i)
   {
      int r = rand()%24;
      cl.push_back(r);
      inv_cl.insert(inv_cl.begin(), inv_clifford_lut_gs[r]);
   }
   cl.insert(cl.begin(),inv_cl.begin(),inv_cl.end());

   k.prepz(0);
   // build the circuit
   for (int i=0; i<num_cliffords; ++i)
      k.clifford(cl[i]);
   k.measure(0);

   return;
}


int main(int argc, char ** argv)
{
   srand(0);

   size_t   num_circuits       = 4;
   size_t   num_qubits         = 1;
   float    sweep_points[]   = { 2, 4, 8, 16 };  // sizes of the clifford circuits per randomization

   // openql runtime options
   ql::options::set("log_level", "LOG_NOTHING");
   ql::options::set("output_dir", "output");
   ql::options::set("optimize", "no");
   ql::options::set("scheduler", "ASAP");
   ql::options::set("use_default_gates", "yes");
   ql::options::set("optimize", "no");
   ql::options::set("decompose_toffoli", "no");

   // create platform
   ql::quantum_platform starmon("starmon","test_cfg_cbox.json");

   // print info
   starmon.print_info();

   // set platform
   ql::set_platform(starmon);

   // ql::sweep_points_t sweep_points;
   
   // create program
   ql::quantum_program rb("rb",starmon,num_qubits,0);

   // set sweep points
   rb.set_sweep_points(sweep_points, num_circuits);
   
   // create kernel
   ql::quantum_kernel kernel("rb16",starmon,num_qubits,0);

   build_rb(16, kernel);

   // kernel.loop(10);

   rb.add(kernel);

   // std::cout<< rb.qasm() << std::endl;

   rb.compile();

   // std::cout << rb.qasm() << std::endl;

   return 0;
}
