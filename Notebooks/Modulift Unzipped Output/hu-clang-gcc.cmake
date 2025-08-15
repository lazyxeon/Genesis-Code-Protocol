include(${CMAKE_SOURCE_DIR}/cmake/modulift/headers.cmake)

set(MODULIFT_PCM_DIR ${CMAKE_BINARY_DIR}/modulift/pcm)
file(MAKE_DIRECTORY ${MODULIFT_PCM_DIR})

foreach(HDR IN LISTS MODULIFT_HEADERS)
  get_filename_component(HDR_BASENAME "${HDR}" NAME_WE)
  if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    set(PCM "${MODULIFT_PCM_DIR}/${HDR_BASENAME}.pcm")
    add_custom_command(
      OUTPUT ${PCM}
      COMMAND "${CMAKE_CXX_COMPILER}" -std=c++20 -fmodule-header "${HDR}" -o "${PCM}"
      DEPENDS ${HDR}
      COMMENT "Clang: -fmodule-header ${HDR} -> ${PCM}"
      VERBATIM)
  else() # GCC
    set(PCM "${MODULIFT_PCM_DIR}/${HDR_BASENAME}.gcm")
    add_custom_command(
      OUTPUT ${PCM}
      COMMAND "${CMAKE_CXX_COMPILER}" -std=c++20 -fmodules-ts -x c++-user-header -c "${HDR}" -o "${PCM}"
      DEPENDS ${HDR}
      COMMENT "GCC: -fmodules-ts -x c++-user-header ${HDR} -> ${PCM}"
      VERBATIM)
  endif()
  list(APPEND MODULIFT_PCMS ${PCM})
endforeach()

function(modulift_target_use_hus TARGET)
  add_custom_target(modulift_build_hus ALL DEPENDS ${MODULIFT_PCMS})
  add_dependencies(${TARGET} modulift_build_hus)
  if (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    foreach(PCM IN LISTS MODULIFT_PCMS)
      target_compile_options(${TARGET} PRIVATE "-fmodule-file=${PCM}")
    endforeach()
  else() # GCC; presence of PCMs + -fmodules-ts enables use
    # GCC typically locates CMIs via include translation; ensure PCMs are built.
  endif()
endfunction()
