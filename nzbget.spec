# TODO: package daemon
Summary:	Binary newsgrabber
Name:		nzbget
Version:	14.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/nzbget/%{name}-%{version}.tar.gz
# Source0-md5:	ade72ca57483a880e1987897a0e4063d
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT

cp -p nzbget.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/nzbget
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nzbget.conf
