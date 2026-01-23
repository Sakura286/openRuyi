# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kexec-tools
Version:        2.0.31
Release:        %autorelease
Summary:        Tools for loading replacement kernels into memory
License:        GPL-2.0-or-later
URL:            https://projects.horms.net/projects/kexec/
VCS:            git:https://git.kernel.org/pub/scm/utils/kernel/kexec/kexec-tools.git
#!RemoteAsset
Source:         https://kernel.org/pub/linux/utils/kernel/kexec/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://kernel.org/pub/linux/utils/kernel/kexec/%{name}-%{version}.tar.sign
BuildSystem:    autotools

Patch1:         add-riscv64-support.patch
Patch2:         riscv-hotplug.patch

BuildOption(conf):  --without-lzma LD=ld.bfd

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)

%description
Kexec is a user space utility for loading another kernel and asking the
currently running kernel to do something with it. A currently running
kernel may be asked to start the loaded kernel on reboot, or to start
the loaded kernel after it panics.

%conf -p
autoreconf -fvi

# No rule to make target 'check'.  Stop.
%check

%files
%{_sbindir}/kexec
%{_mandir}/man8/kexec.8*
%{_sbindir}/vmcore-dmesg
%{_mandir}/man8/vmcore-dmesg.8*
%ifarch x86_64
%{_libdir}/kexec-tools/kexec_test
%endif

%doc News
%license COPYING
%doc TODO

%changelog
%{?autochangelog}
