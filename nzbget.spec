Summary:	Binary newsgrabber.
Summary(pl.UTF-8):	-
Name:		nzbget
Version:	0.5.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/nzbget/%{name}-%{version}.tar.gz
# Source0-md5:	3ff7cb297bbe0fd3aa378343849d85f1
URL:		http://nzbget.sourceforge.net/
BuildRequires:	gnutls-devel
BuildRequires:	libpar2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NZBGet is a binary newsgrabber, which downloads files from usenet
based on information given in nzb-files. NZBGet can be used in
standalone and in server/client modes. In standalone mode you pass a
nzb-file as parameter in command-line, NZBGet downloads listed files
and then exits.

In server/client mode NZBGet runs as server in background. Then you
use client to send requests to server. The sample requests are:
download nzb-file, list files in queue, etc.

Standalone-tool, server and client are all contained in only one
executable file "nzbget". The mode in which the program works depends
on command-line parameters passed to the program.

%description -l pl.UTF-8

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README nzbget.conf.example
%attr(755,root,root) %{_bindir}/*
