# Disable byte compiling
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Summary:    Analysis of space and usage of disk
Name:       nethserver-duc
Version:    0.0.1
Release:    1%{?dist}
License:    GPL
URL:        %{url_prefix}/%{name}
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch

Requires:   nethserver-base
Requires:   duc

BuildRequires: perl
BuildRequires: nethserver-devtools

%description
Visualize the space and the usage of your disk.

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist
grep -v -E '(xml2json.pyc|xml2json.pyo)' %{name}-%{version}-filelist > tmp-filelist
mv tmp-filelist %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Mon Feb 9 2015 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0
- first release