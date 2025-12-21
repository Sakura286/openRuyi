# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spdk
Version:        25.09
Release:        %autorelease
Summary:        Set of libraries and utilities for high performance user-mode storage
License:        BSD and MIT
URL:            http://spdk.io
#!RemoteAsset
Source0:        https://github.com/spdk/spdk/archive/refs/tags/v%{version}.tar.gz

BuildSystem:    autotools

BuildOption(install): libdir=%{_libdir}

%define package_version %{version}-%{release}

BuildRequires:  make
BuildRequires:  dpdk-devel
BuildRequires:  numactl-devel
BuildRequires:  ncurses-devel
BuildRequires:  libaio-devel
BuildRequires:  openssl-devel
BuildRequires:  fuse3
BuildRequires:  fuse3-devel
BuildRequires:  python-devel
BuildRequires:  python-pip
BuildRequires:  python-setuptools
BuildRequires:  python-wheel
BuildRequires:  python-hatchling
BuildRequires:  util-linux-devel
BuildRequires:  patchelf

Requires:       dpdk
Requires:       numactl
Requires:       openssl
# TODO: Enable it when we have these two BuildRequires
# NVMe over Fabrics
#Requires:       librdmacm
#Requires:       libiscsi
Requires:       libaio
Requires:       libuuid
Requires:       fuse3

%description
The Storage Performance Development Kit provides a set of tools
and libraries for writing high performance, scalable, user-mode storage
applications.

%package        devel
Summary:        Storage Performance Development Kit development files
Requires:       %{name}%{?_isa} = %{package_version}
Provides:       %{name}-static%{?_isa} = %{package_version}

%description    devel
This package contains the headers and other files needed for
developing applications with the Storage Performance Development Kit.

%package        static
Summary:        Storage Performance Development Kit static libraries
Requires:       %{name}-devel%{?_isa} = %{package_version}

%description    static
This package contains the static libraries for the Storage Performance
Development Kit.

%package        tools
Summary:        Storage Performance Development Kit tools files
Requires:       %{name} = %{package_version}
BuildArch:      noarch

%description    tools
%{summary}

# not utilize a standard configure script.
%conf
export LD=ld.bfd
export CC="gcc -fuse-ld=bfd"
export CXX="g++ -fuse-ld=bfd"

./configure --prefix=%{_usr} \
	--libdir=%{_libdir} \
	--with-dpdk \
	--disable-examples \
	--disable-tests \
	--disable-unit-tests \
	--with-shared

%install -p
find . -name "*.mk" -o -name "Makefile" | xargs sed -i 's/pip install/pip install --no-build-isolation/g'

%install -a

# Create self-contained spdk-setup script (similar to PKGBUILD approach)
echo '#!/usr/bin/env bash' > %{buildroot}%{_bindir}/spdk-setup
cat scripts/common.sh scripts/setup.sh >> %{buildroot}%{_bindir}/spdk-setup
sed -ri '/^rootdir/d;/^source/d;s,\$rootdir,%{_usr},' %{buildroot}%{_bindir}/spdk-setup
chmod +x %{buildroot}%{_bindir}/spdk-setup

# Install bash completion
install -Dm644 scripts/bash-completion/spdk %{buildroot}%{_datadir}/bash-completion/completions/spdk

# Install license
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

# Install tools
mkdir -p %{buildroot}%{_datadir}/%{name}
find scripts -type f -regextype egrep -regex '.*(spdkcli|rpc).*[.]py' \
	-exec cp --parents -t %{buildroot}%{_datadir}/%{name} {} ";"

# no tests
%check

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%{_bindir}/spdk-setup
%{python_sitelib}/spdk*/*
%{_bindir}/nvmf_tgt
%{_bindir}/iscsi_tgt
%{_bindir}/vhost
%{_bindir}/spdk_*
%{_libdir}/*.so.*
%{_datadir}/bash-completion/completions/spdk

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_libdir}/*.so

%files static
%{_libdir}/*.a

%files tools
%{_datadir}/%{name}/scripts
%{_bindir}/spdk-cli
%{_bindir}/spdk-mcp
%{_bindir}/spdk-rpc
%{_bindir}/spdk-sma

%changelog
%{?autochangelog}
