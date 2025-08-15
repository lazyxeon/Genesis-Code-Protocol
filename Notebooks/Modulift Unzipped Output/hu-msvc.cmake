\
include(${CMAKE_SOURCE_DIR}/cmake/modulift/headers.cmake)

# Directory for IFC artifacts and the TOML map
set(MODULIFT_IFC_DIR ${CMAKE_BINARY_DIR}/modulift/ifc)
file(MAKE_DIRECTORY ${MODULIFT_IFC_DIR})
set(MODULIFT_IFC_MAP ${CMAKE_BINARY_DIR}/modulift/ifc-map.toml)

# 1) Precompile each header as a header unit (.ifc)
foreach(HDR IN LISTS MODULIFT_HEADERS)
  get_filename_component(HDR_BASENAME "${HDR}" NAME)
  set(IFC "${MODULIFT_IFC_DIR}/${HDR_BASENAME}.ifc")
  add_custom_command(
    OUTPUT ${IFC}
    COMMAND "${CMAKE_CXX_COMPILER}" /nologo /std:c++20 /EHsc /TP
            /ifcOutput "${MODULIFT_IFC_DIR}\\"
            /exportHeader "${HDR}"
    DEPENDS ${HDR}
    COMMENT "MSVC: exportHeader ${HDR} -> ${IFC}"
    VERBATIM
  )
  list(APPEND MODULIFT_IFCS ${IFC})

  # Build TOML entries (quote lookup for headers)
  string(APPEND MODULIFT_IFC_TOML
"[[header-unit]]\nname = ['quote', '${HDR_BASENAME}']\nifc  = '${IFC}'\n")
endforeach()

# 2) Write the IFC map (TOML) for /ifcMap
file(WRITE  ${MODULIFT_IFC_MAP} "${MODULIFT_IFC_TOML}")

# 3) Public function to wire a target to consume the HU map
function(modulift_target_use_hus TARGET)
  add_custom_target(modulift_build_hus ALL DEPENDS ${MODULIFT_IFCS})
  add_dependencies(${TARGET} modulift_build_hus)
  target_compile_options(${TARGET} PRIVATE "/std:c++20" "/ifcMap:${MODULIFT_IFC_MAP}")
endfunction()
