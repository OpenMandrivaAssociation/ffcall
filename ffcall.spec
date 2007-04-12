%define	name	ffcall
%define	version	1.10
%define	release	%mkrel 2

%define major 0
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} %{major} -d

Summary:	Libraries that can be used to build foreign function call interfaces.
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/C
URL:		ftp://ftp.santafe.edu/pub/gnu/
Source:		ftp://ftp.santafe.edu/pub/gnu/%{name}-%{version}.tar.bz2
Buildrequires:	autoconf2.5

%package        -n %{libnamedev}
Summary:	Libraries that can be used to build foreign function call interfaces. 
Group:          Development/Other
Provides:	%{libname}-devel
Provides:	libffcall-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
    (a reentrant combination of vacall and trampoline)

    This version B includes some minor configuration changes so that files
    are installed in the proper place. Also it compiles on cygwin and mingw32.


%description -n %{libnamedev}
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
               (a reentrant combination of vacall and trampoline)

This version B includes some minor configuration changes so that files
are installed in the proper place. Also it compiles on cygwin and mingw32.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --enable-shared
make

%install
rm -rf %buildroot

mkdir -p %buildroot %buildroot/%_includedir %buildroot/%_libdir %buildroot/%_mandir
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{libnamedev}-%{version}
mv $RPM_BUILD_ROOT/usr/share/html $RPM_BUILD_ROOT%{_defaultdocdir}/%{libnamedev}-%{version}/html

%post -n %{libnamedev} -p /sbin/ldconfig
%postun	-n %{libnamedev} -p /sbin/ldconfig

%clean
rm -rf %buildroot

%files -n %{libnamedev}
%defattr(-,root,root)
%doc COPYING NEWS README PLATFORMS
%_includedir/*
%{_libdir}/*
%{_mandir}/man3/*


