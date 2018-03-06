#
# Find DOUBLE_CONVERSION
#
#  DOUBLE_CONVERSION_INCLUDE_DIR - where to find double-conversion/double-conversion.h, etc.
#  DOUBLE_CONVERSION_LIBRARY     - List of libraries when using libdouble-conversion.
#  DOUBLE_CONVERSION_FOUND       - True if libdouble-conversion found.

FIND_PATH(DOUBLE_CONVERSION_INCLUDE_DIR double-conversion/double-conversion.h)

FIND_LIBRARY(DOUBLE_CONVERSION_LIBRARY NAMES double-conversion)

# handle the QUIETLY and REQUIRED arguments and set DOUBLE_CONVERSION_FOUND to TRUE if
# all listed variables are TRUE
INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DOUBLE_CONVERSION DEFAULT_MSG DOUBLE_CONVERSION_LIBRARY DOUBLE_CONVERSION_INCLUDE_DIR)

MARK_AS_ADVANCED(DOUBLE_CONVERSION_LIBRARY DOUBLE_CONVERSION_INCLUDE_DIR)

