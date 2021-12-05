%define major 1
%define oldmajor 0
%define libavcall		%mklibname avcall		%{major}
%define libcallback		%mklibname callback		%{major}
%define libtrampoline	%mklibname trampoline	%{major}
%define libffcall		%mklibname ffcall		%{oldmajor}

%define devname			%mklibname %{name} -d

Summary:	Libraries that can be used to build foreign function call interfaces
Name:		ffcall
Version:	2.4
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnu.org/software/lib%{name}
Source:		https://ftp.gnu.org/gnu/libffcall/lib%{name}-%{version}.tar.gz
Patch0:		ffcall-make-jN.patch
# Upstream is dead, so this patch will not be sent. Update some uses of OABI
# on ARM to their EABI equivalents.
#Patch1:	 %{name}-arm.patch
# (upstream commit 580f0bb144c0d63560c61229291e172e55971437
Patch10:	ffcall.git-03c892dd77f910220da7621e1596635890f5e146.patch
Patch11:	ffcall.git-580f0bb144c0d63560c61229291e172e55971437.patch

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

#----------------------------------------------------------------------------

%package -n %{libavcall}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
Conflicts:	%{_lib}ffcall0 < 1.10-11

%description -n %{libavcall}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libavcall}
%{_libdir}/libavcall.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libcallback}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
Conflicts:	%{_lib}ffcall0 < 1.10-11
Obsoletes:	%{_lib}ffcall0 < 1.10-11

%description -n %{libcallback}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libcallback}
%{_libdir}/libcallback.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libffcall}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
Conflicts:	%{_lib}ffcall0 < 1.10-11
Obsoletes:	%{_lib}ffcall0 < 1.10-11

%description -n %{libffcall}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libffcall}
%{_libdir}/libffcall.so.%{oldmajor}*

#----------------------------------------------------------------------------
%package -n %{libtrampoline}
Summary:	Libraries that can be used to build foreign function call interfaces
Group:		System/Libraries
Conflicts:	%{_lib}ffcall0 < 1.10-11
Obsoletes:	%{_lib}ffcall0 < 1.10-11

%description -n %{libtrampoline}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

It consists of two parts:
 * avcall - calling C functions with variable arguments.
   Its include file is <avcall.h>.
 * callback - closures with variable arguments as first-class C functions.
   Its include file is <callback.h>.

Additionally, you can determine the libffcall version by including
<ffcall-version.h>.

For backward compatibility with versions 1.x, libraries libavcall.{a,so}
and libcallback are installed as well. But they are deprecated;
use libffcall instead.

%files -n %{libtrampoline}
%{_libdir}/libtrampoline.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for ffcall library
Group:		Development/C
Requires:	%{libavcall} = %{EVRD}
Requires:	%{libcallback} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for ffcall library.

%files -n %{devname}
%doc NEWS README PLATFORMS
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*
%{_defaultdocdir}/%{devname}/html

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n lib%{name}-%{version}

%build
%ifarch %arm
export CC=gcc
export CXX=g++
%endif

%configure
%make_build -j1

%install
%make_install

# fix doc path
mkdir -p %{buildroot}%{_defaultdocdir}/%{devname}
mv %{buildroot}%{_datadir}/html %{buildroot}%{_defaultdocdir}/%{devname}/html

