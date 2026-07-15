#include <pybind11/pybind11.h>
#include "MAI_LIB/NN/MAI.hpp"
namespace py = pybind11;
PYBIND11_MODULE(mai, m)
{
    py::class_<MAI>(m,"MAI")
        .def(py::init<>())
        .def(
            "create",
            &MAI::create
        )
        .def(
            "process_and_memorize",
            &MAI::process_and_memorize
        )
        .def(
            "process",
            &MAI::process
        )
        .def(
            "add_ND",
            &MAI::add_ND
        )
        .def(
            "add_NP",
            &MAI::add_NP
        )
        .def(
            "map",
            &MAI::map
        )
        .def(
            "ajust_TA",
            &MAI::ajust_TA
        );
}