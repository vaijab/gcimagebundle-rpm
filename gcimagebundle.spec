%define name gcimagebundle
%define version 1.1.0
%define unmangled_version 1.1.0
%define release 1

Summary: Image bundling tool for root file system.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  python2-devel >= 2.4, python-setuptools
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Google Inc. <gc-team@google.com>
Url: https://github.com/GoogleCloudPlatform/compute-image-packages/tree/master/image-bundle

%description
Image Bundle is a python package that allows users to create an image from the
current state of the running virtual machine. Image Bundle creates the image
with the recommended packaging format and also allows you to run unit tests to
verify that image bundle works properly on your operating system. See [Custom
Images](https://developers.google.com/compute/docs/images#bundle_image) for
more information.

%prep
%setup -q -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
