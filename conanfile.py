from conans import ConanFile, CMake
import os

class StringIdConan(ConanFile):
  name = "string_id"
  version = "2.0-2"
  description = "A small C++ library to handle hashed strings serving as identifiers."
  license="Modified BSD License (3-Clause BSD license)"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-stringid"

  def source(self):
    self.run("git clone https://github.com/foonathan/string_id")
    os.chdir("string_id")
    self.run("git checkout v2.0-2")

  def build(self):
    os.makedirs("string_id/build")
    os.chdir("string_id/build")
    self.run("cmake ..")
    self.run("cmake --build .")

  def package(self):
    self.copy("*.hpp", dst="include", keep_path=False)
    self.copy("*.hpp.in", dst="include", keep_path=False)
    self.copy("*.lib", dst="lib", keep_path=False)
    self.copy("*.a", dst="lib", keep_path=False)
