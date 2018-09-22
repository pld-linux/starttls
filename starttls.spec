#
# Conditional build:
%bcond_without	emacs		# Build without GNU Emacs support
%bcond_without	xemacs		# Build without XEmacs support
#
Summary:	A simple wrapper program for STARTTLS
Summary(pl.UTF-8):	Prosty program obudowujący dla STARTTLS
Name:		starttls
Version:	0.10
Release:	5
License:	GPL
Group:		Applications
Source0:	ftp://ftp.opaopa.org/pub/elisp/%{name}-%{version}.tar.gz
# Source0-md5:	2e0d26b0db04bae813248eb5af7e9205
BuildRequires:	openssl-devel
%if %{with emacs}
BuildRequires:  emacs
%{?with_xemacs:BuildRequires:  xemacs}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
starttls - simple wrapper program for STARTTLS.

%description -l pl.UTF-8
starttls - prosty program obudowujący dla STARTTLS.

%package emacs
Summary:	Lisp utility functions for STARTTLS profiles
Summary(pl.UTF-8):	Funkcje narzędziowe Lispa dla profili STARTTLS
Group:		Applications/Editors/Emacs
Requires:	%{name} = %{version}-%{release}
Requires:	emacs

%description emacs
Lisp module that defines some utility functions for STARTTLS profiles.

%description emacs -l pl.UTF-8
Moduł Lispa definiujący funkcje narzędziowe dla profili STARTTLS.

%package xemacs
Summary:	Lisp utility functions for STARTTLS profiles
Summary(pl.UTF-8):	Funkcje narzędziowe Lispa dla profili STARTTLS
Group:		Applications/Editors/Emacs
Requires:	%{name} = %{version}-%{release}
Requires:	xemacs

%description xemacs
Lisp module that defines some utility functions for STARTTLS profiles.

%description xemacs -l pl.UTF-8
Moduł Lispa definiujący funkcje narzędziowe dla profili STARTTLS.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs/site-lisp

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/* \
	$RPM_BUILD_ROOT%{_datadir}/xemacs/site-lisp/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README starttls.el
%attr(755,root,root) %{_bindir}/*

%if %{with emacs}
%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/*

%if %{with xemacs}
%files xemacs
%defattr(644,root,root,755)
%{_datadir}/xemacs/site-lisp/*
%endif
%endif
