# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scikit-learn
%global modname scikit_learn

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        Machine learning in Python
# sklearn/externals/_arff.py is MIT
# sklearn/externals/_packaging is BSD-2-Clause
# sklearn/metrics/_scorer.py is BSD-2-Clause
# sklearn/datasets/images/china.jpg  is CC-BY-2.0
# sklearn/datasets/images/flower.jpg is CC-BY-2.0
# sklearn/utils/_pprint.py is PSF-2.0
License: BSD-3-Clause AND CC-BY-2.0 AND MIT AND BSD-2-Clause AND PSF-2.0
URL:            http://scikit-learn.org/
VCS:            git:https://github.com/scikit-learn/scikit-learn
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{modname}/%{modname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  sklearn

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(torch)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Scikit-learn integrates machine learning algorithms in the tightly-knit 
scientific Python world, building upon numpy, scipy, and matplotlib. 
As a machine-learning module, it provides versatile tools for data mining 
and analysis in any field of science and engineering. It strives to be 
simple and efficient, accessible to everybody, and reusable 
in various contexts.

%prep -a
sed -i -e 's|numpy>=2,<2.4.0|numpy|' pyproject.toml
sed -i -e 's|scipy>=1.10.0,<1.17.0|scipy|' pyproject.toml

%generate_buildrequires
# meson build cannot provide build metadata before build
%pyproject_buildrequires -p

# Some test requirements are not satisfied on openRuyi
%check

%files -f %{pyproject_files}
%license COPYING sklearn/svm/src/liblinear/COPYRIGHT
%doc examples/

%changelog
%{?autochangelog}
