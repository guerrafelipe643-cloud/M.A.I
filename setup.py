# ==============================================================================
#   MAI - Memory Architecture for AI (Arquitetura Modular para IA)
#   Copyright (C) 2026  Felipe Guerra Rodrigues Athaydes
#
#   Este programa é um software livre: você pode redistribuí-lo e/ou modificá-lo
#   sob os termos da Licença Pública Geral GNU conforme publicada pela
#   Free Software Foundation, tanto a versão 3 da Licença, ou (a seu critério)
#   qualquer versão posterior.
#
#   Este programa é distribuído na expectativa de que seja útil, mas
#   SEM NENHUMA GARANTIA; sem mesmo a garantia implícita de
#   COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO. Veja a
#   Licença Pública Geral GNU para mais detalhes.
#
#   Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com
#   este programa. Se não, veja <https://gnu.org>.
# ==============================================================================
from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup
setup(
    name="mai",
    ext_modules=[
        Pybind11Extension(
            "mai",
            [
                "MAI_LIB_py/binding.cpp",
                "src/MAI_LIB.cpp",
                "src/MAI_ND.cpp",
                "src/MAI_NP.cpp"
            ],
            include_dirs=[
                "."
            ]
        )
    ]
)