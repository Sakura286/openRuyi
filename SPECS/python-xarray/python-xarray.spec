# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: add cupy on openRuyi
%bcond cupy 0
# TODO: xarray and dask requires each other
%bcond bootstrap 1
# TODO: need sparse as an option. but sparse need numba.
# There is no numba on oR.
%bcond sparse 0

%global srcname xarray

Name:           python-%{srcname}
Version:        2026.2.0
Release:        %autorelease
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
URL:            https://github.com/pydata/xarray
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch0:         0001-Fix-encoding-of-masked-dask-arrays-11157.patch

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(array-api-strict)
BuildRequires:  python3dist(cftime)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pint)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
%{?with_cupy:BuildRequires:  python3dist(cupy)}
%{?with_sparse:BuildRequires:  python3dist(sparse)}
%{!?with_bootstrap:BuildRequires:  python3dist(dask)}


Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Xarray (formerly xray) is an open source project and Python package that
makes working with labelled multi-dimensional arrays simple, efficient,
and fun!

Xarray introduces labels in the form of dimensions, coordinates and
attributes on top of raw NumPy-like arrays, which allows for a more
intuitive, more concise, and less error-prone developer experience. The
package includes a large and growing library of domain-agnostic functions
for advanced analytics and visualization with these data structures.

Xarray was inspired by and borrows heavily from pandas, the popular data
analysis package focused on labelled tabular data. It is particularly
tailored to working with netCDF files, which were the source of xarray
data model, and integrates tightly with dask for parallel computing.

%generate_buildrequires
%pyproject_buildrequires

%check
%{pyproject_check_import %{!?with_cupy:-e 'xarray.tests.test_cupy'} \
    %{?with_bootstrap:-e 'xarray.tests.test_dask' -e 'xarray.tests.test_distributed'} \
    %{!?with_sparse: -e 'xarray.tests.test_sparse'}
}

rm -rf xarray
echo >> pytest.ini  # Ignore any command-line arguments from upstream.
pytest_args=(
  -n auto
  -m "not network"
# bug: test is too old for pandas
  --deselect "tests/test_dataset.py::TestDataset::test_repr"
# TODO: fix this
  --deselect "tests/test_variable.py::TestIndexVariable::test_concat_periods"
# bug: test is too old for numpy
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit[False]"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit[True]"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit_helpers"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit_multidimensional_guess[False]"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit_multidimensional_guess[True]"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit_multidimensional_bounds[False]"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit_multidimensional_bounds[True]"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit_ignore_errors[False]"
  --deselect "tests/test_dataarray.py::TestDataArray::test_curvefit_ignore_errors[True]"
  --deselect "tests/test_groupby.py::TestDataArrayResample::test_upsample_interpolate"
  --deselect "tests/test_interp.py::test_interpolate_1d[no_chunk-x-cubic]"
  --deselect "tests/test_interp.py::test_interpolate_1d[no_chunk-y-cubic]"
  --deselect "tests/test_interp.py::test_interpolate_1d_methods[cubic]"
  --deselect "tests/test_interp.py::test_decompose[slinear]"
  --deselect "tests/test_interp.py::test_interpolate_nd[no_chunk-cubic]"
  --deselect "tests/test_interp.py::test_interpolate_nd[no_chunk-quintic]"
  --deselect "tests/test_interp.py::test_interpolate_nd[no_chunk-slinear]"
  --deselect "tests/test_interp.py::test_interpolate_nd_nd[slinear]"
  --deselect "tests/test_missing.py::test_interpolate_pd_compat[quadratic-None]"
  --deselect "tests/test_missing.py::test_interpolate_pd_compat[quadratic-nan]"
  --deselect "tests/test_missing.py::test_interpolate_pd_compat[quadratic-47.11]"
  --deselect "tests/test_missing.py::test_interpolate_pd_compat[cubic-None]"
  --deselect "tests/test_missing.py::test_interpolate_pd_compat[cubic-nan]"
  --deselect "tests/test_missing.py::test_interpolate_pd_compat[cubic-47.11]"
  --deselect "tests/test_missing.py::test_interpolate_methods"
  --deselect "tests/test_missing.py::test_interpolate_pd_compat_polynomial"
)
%pytest "${pytest_args[@]}" --pyargs xarray

%files -f %{pyproject_files}
%license licenses/*
%doc README.md

%changelog
%{?autochangelog}
