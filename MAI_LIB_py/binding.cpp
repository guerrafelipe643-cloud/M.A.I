// ===============================================================================
//   MAI - Memory Architecture for AI (Arquitetura de memória para IA)
//   Copyright (C) 2026  Felipe Guerra Rodrigues Athaydes
//
//   Este programa é um software livre: você pode redistribuí-lo e/ou modificá-lo
//   sob os termos da Licença Pública Geral GNU conforme publicada pela
//   Free Software Foundation, tanto a versão 3 da Licença, ou (a seu critério)
//   qualquer versão posterior.
//
//   Este programa é distribuído na expectativa de que seja útil, mas
//   SEM NENHUMA GARANTIA; sem mesmo a garantia implícita de
//   COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO. Veja a
//   Licença Pública Geral GNU para mais detalhes.
//
//  Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com
//   este programa. Se não, veja <https://gnu.org>.
// ==============================================================================
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
