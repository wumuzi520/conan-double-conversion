#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class DoubleConversionConan(ConanFile):
    name = "double-conversion"
    version = "3.0.0"
    url = "https://github.com/google/double-conversion"
    description = "Efficient binary-decimal and decimal-binary conversion routines for IEEE doubles."
    license = "https://github.com/google/double-conversion/blob/master/LICENSE"
    generators = "cmake"
    exports_sources = ["CMakeLists.txt"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    requires = ""

    def configure(self):
        del self.settings.compiler.libcxx

        if self.settings.os == "Windows":
            self.options.remove("fPIC")

    def source(self):
        source_url = "https://github.com/google/double-conversion"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        if self.settings.os != "Windows":
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("sources/LICENSE", dst="licenses", keep_path=False)
        self.copy(pattern="*.h", dst="include/double-conversion", src="sources/double-conversion")
        with tools.chdir("sources"):
            self.copy(pattern="*.dll", dst="bin", keep_path=False)
            if self.settings.build_type == "Debug":
                self.copy(pattern="*.pdb", dst="bin", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", keep_path=False)
            if self.options.shared == True:
                self.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)
                self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)
            else:
                self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
