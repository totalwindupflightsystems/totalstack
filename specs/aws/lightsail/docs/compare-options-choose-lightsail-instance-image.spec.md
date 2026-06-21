---
id: "@specs/aws/lightsail/docs/compare-options-choose-lightsail-instance-image"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Blueprints"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Blueprints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/compare-options-choose-lightsail-instance-image
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Review the Lightsail instance blueprint offerings
<a name="compare-options-choose-lightsail-instance-image"></a>

Lightsail provides several options for you to create your virtual private server. This topic helps you decide which operating system (OS), application, or development stack is right for your project. We organized the applications by functional area (such as CMS and ecommerce).

## Operating systems
<a name="compare-operating-systems"></a>

Lightsail has several Linux/Unix-based or Windows-based operating systems to choose from.

** **Windows Server 2022** **  
Lightsail running Windows Server is a fast and dependable environment for deploying applications using the Microsoft Web Platform. With Lightsail, you can run any compatible Windows-based solution on the high-performance, reliable, cost-effective AWS Cloud computing platform. Common Windows use cases include Enterprise Windows-based application hosting, website and web service hosting, data processing, distributed testing, ASP.NET application hosting, and any other application requiring Windows software. For end of support information, see the [https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2022](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2022) website.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [Windows Server 2022](https://aws.amazon.com/marketplace/pp/prodview-dq4sxno5vuy7m). 

** **Windows Server 2019** **  
Lightsail running Windows Server is a fast and dependable environment for deploying applications using the Microsoft Web Platform. Lightsail enables you to run any compatible Windows-based solution on the high-performance, reliable, cost-effective AWS cloud computing platform. Common Windows use cases include Enterprise Windows-based application hosting, website and web service hosting, data processing, distributed testing, ASP.NET application hosting, and any other application requiring Windows software. For end of support information, see the [https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2019](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2019) website.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [Windows Server 2019](https://aws.amazon.com/marketplace/pp/B07QZ4XZ8F). 

** **Windows Server 2016** **  
Lightsail running Windows Server is a fast and dependable environment for deploying applications using the Microsoft Web Platform. Lightsail enables you to run any compatible Windows-based solution on the high-performance, reliable, cost-effective AWS cloud computing platform. Common Windows use cases include Enterprise Windows-based application hosting, website and web service hosting, data processing, distributed testing, ASP.NET application hosting, and any other application requiring Windows software. For end of support information, see the [https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016) website.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [Windows Server 2016](https://aws.amazon.com/marketplace/pp/B01M7SJEU7). 

****Amazon Linux 2023****  
Amazon Linux 2023 (AL2023) is the next generation of Amazon Linux, ideal for general purpose workloads on AWS. AL2023 will be supported for five years after it is generally available. AL2023 locks to a specific version of the Amazon Linux package repository, giving you control over how and when you absorb updates. AL2023 also provides the ability to get frequent updates and comes with features to help you meet your compliance needs.  
Lightsail instances launched from AL2023 will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/).

** **Amazon Linux 2** **  
Amazon Linux 2 will reach End of Long Term Support on June 30, 2026. You will not be able to create new Lightsail instances with this blueprint on or after June 30, 2026. For more information, see the [Amazon Linux 2 website](https://aws.amazon.com/amazon-linux-2/faqs/).
Amazon Linux 2 is the previous generation of Amazon Linux, a Linux server operating system from AWS. It provides a secure, stable, and high performance execution environment to develop and run cloud and enterprise applications. With Amazon Linux 2, you get an application environment that offers long term support with access to the latest innovations in Linux. Amazon Linux 2 is provided at no additional charge. For end of support information, see [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/).  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [ Amazon Linux 2](https://aws.amazon.com/amazon-linux-2).

** **AlmaLinux OS 9** **  
AlmaLinux OS 9 is an open source, community owned and governed, forever-free enterprise Linux distribution, focused on long-term stability, providing a robust production-grade platform. AlmaLinux is compatible with RHEL® and pre-Stream CentOS. For end of support information, see the [https://almalinux.org](https://almalinux.org) website.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [AlmaLinux OS 9](https://aws.amazon.com/marketplace/pp/prodview-ykmb6re2rcouy).

** **CentOS Stream 9** **  
CentOS Stream 9 is the next major release of the CentOS Stream distribution. CentOS Stream 9 is a continuously delivered distribution that tracks just ahead of Red Hat Enterprise Linux (RHEL) development, positioned as a midstream between Fedora Linux and RHEL. It's designed to be functionally compatible with RHEL and provides a stable, predictable, manageable and reproducible Linux environment. For end of support information, see the [CentOS](https://www.centos.org/) website.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more at the [https://www.centos.org/centos-stream/](https://www.centos.org/centos-stream/) website.

** **Debian 11, 12, and 13** **  
Debian 11 will reach End of Long Term Support on August 31, 2026. You will not be able to create new Lightsail instances with this blueprint on or after August 31, 2026. For more information, see the [Debian website](https://wiki.debian.org/LTS).
Debian is a free operating system, developed by thousands of volunteers from all over the world who collaborate over the internet. The Debian project's key strengths are its volunteer base, its dedication to the Debian Social Contract and Free Software, and its commitment to provide the best operating system possible. This new release is another important step in that direction. For end of support information, see the [Debian website](https://wiki.debian.org/DebianReleases).  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more at the [https://www.debian.org/doc/](https://www.debian.org/doc/) website.

** **FreeBSD 14 and 15** **  
FreeBSD is an operating system used to power servers, desktops, and embedded systems. Derived from BSD, the version of UNIX developed at the University of California, Berkeley, FreeBSD has been continually developed by a large community for more than 30 years. FreeBSD's networking, security, storage, and monitoring features, including the pf firewall, the Capsicum and CloudABI capability frameworks, the ZFS file system, and the DTrace dynamic tracing framework, make FreeBSD the platform of choice for many of the busiest websites and most pervasive embedded networking and storage systems. For end of support information, see the [https://www.freebsd.org/security/#sup](https://www.freebsd.org/security/#sup) website.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more at the [https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/](https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/) website.

** **openSUSE 15 and 16** **  
openSUSE Leap 15 will reach End of Life on July 30, 2026. You will not be able to create new Lightsail instances with the openSUSE 15 blueprint on or after July 30, 2026. For more information, see the [https://en.opensuse.org/](https://en.opensuse.org/) website.
The openSUSE distribution is a stable, easy to use and complete multipurpose Linux distribution. It is aimed towards users and developers working on the desktop or server. It is great for beginners, experienced users and ultra geeks alike, in short, it is perfect for everybody\! For end of support information, see the [https://en.opensuse.org/](https://en.opensuse.org/) website.  
Password authentication is disabled by default for this operating system. This means that even if you create an instance from a snapshot of an instance with password authentication enabled, the new instance will have password authentication disabled. For more information about password authentication in SUSE Linux, see [document 3404214](https://www.suse.com/support/kb/doc/?id=000016192) in the SUSE documentation.  
To log in to your instance with password authentication disabled, you can use the browser-based SSH client on the Lightsail console or a key pair. For more information about logging in, see [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md) or [Connect to Lightsail Linux or Unix instances with the SSH command](amazon-lightsail-ssh-using-terminal.md).  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more at the [https://www.opensuse.org/](https://www.opensuse.org/) website.

** **Ubuntu 22 and 24** **  
Ubuntu Server is a Debian-based Linux operating system used for virtual servers. A default installation of Ubuntu contains a wide range of software that includes LibreOffice, Firefox, Thunderbird, and Transmission. You can install many additional software packages, such as Evolution, GIMP, Pidgin, and Synaptic by using the APT-based package management tool (`apt-get`). For end of support information, see the [https://wiki.ubuntu.com/Releases](https://wiki.ubuntu.com/Releases) website.  
Lightsail instances created with the Ubuntu 24 blueprint will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more at the [https://help.ubuntu.com/community/CommunityHelpWiki](https://help.ubuntu.com/community/CommunityHelpWiki) website.

## Database applications
<a name="compare-database-applications"></a>

The following database applications are available in Lightsail:

** **SQL Server 2022 Express** **  
SQL Server Express is a relational database management system that is free to download, distribute, and use. It comprises a database specifically targeted for embedded and smaller-scale applications. This Lightsail image runs on a base OS of Windows Server 2022.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [SQL Server 2022 Express](https://aws.amazon.com/marketplace/pp/prodview-c2jz4lr4h2yc6).

** **SQL Server 2019 Express** **  
SQL Server Express is a relational database management system that is free to download, distribute, and use. It comprises a database specifically targeted for embedded and smaller-scale applications. This Lightsail image runs on a base OS of Windows Server 2022.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about [SQL Server 2019 Express](https://aws.amazon.com/marketplace/pp/prodview-xbikutlmywslu).

** **SQL Server 2016 Express** **  
SQL Server 2016 Express will reach End of Extended Support on July 14, 2026. You will not be able to create new Lightsail instances with this blueprint on or after July 14, 2026. For more information, see the [Microsoft website](https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2016).
SQL Server Express is a relational database management system that is free to download, distribute, and use. It comprises a database specifically targeted for embedded and smaller-scale applications. This Lightsail image runs on a base OS of Windows Server 2016.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
 Learn more about [SQL Server 2016 Express](https://aws.amazon.com/marketplace/pp/B01MAZHH98).

## CMS applications
<a name="compare-cms-applications"></a>

The following content management system (CMS) applications are available in Lightsail:

** **WordPress** **  
 The WordPress blueprint provides a complete production environment with PHP, MariaDB, phpMyAdmin, and WordPress. This blueprint supports Lightsail’s guided workflow for configuring HTTPS with Let’s Encrypt SSL certificates with just a few clicks. Popular plugins like Jetpack, All in One SEO, WP Mail, Google Analytics for WordPress, All-in-One WP Migration and Backup, AMP, and W3 Total Cache are pre-installed in this blueprint.   
Lightsail instances launched from WordPress will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
[Launch and configure a WordPress instance](amazon-lightsail-launch-and-configure-wordpress.md)  
Learn more about the [WordPress stack](https://wordpress.org/) at the *WordPress* website.

** **WordPress certified by Bitnami** **  
Bitnami WordPress is a preconfigured, ready-to-use image for running WordPress on Lightsail. WordPress is a popular web publishing platform for building blogs and websites. You can customize it by using a wide selection of themes, extensions, plugins, and widgets.  
 WordPress features a full theme system, which enables you to change the look and feel of your site with a few clicks. You can also use existing free or commercial WordPress themes. WordPress is in full compliance with the standards of the [https://www.w3.org/](https://www.w3.org/).  
[WordPress by Bitnami](amazon-lightsail-wordpress-bitnami.md)  
Learn more about [WordPress](https://bitnami.com/stack/wordpress) at the *Bitnami* website.

** **WordPress Multisite** **  
 The WordPress Multisite blueprint provides a complete production environment with PHP, MariaDB, phpMyAdmin, and WordPress. Lightsail packages blueprints to be secure and up-to-date using industry best practices.   
Lightsail instances launched from WordPress Multisite will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
[Set up WordPress Multisite on Lightsail](amazon-lightsail-quick-start-guide-wordpress-multisite.md)  
Learn more about [WordPress Multisite](https://developer.wordpress.org/advanced-administration/multisite/) at the *WordPress* website.

** **WordPress Multisite certified by Bitnami** **  
WordPress Multisite enables administrators to host and manage multiple websites from the same WordPress instance. These websites can all have unique domain names and can be customized by their owners, while sharing assets such as themes and plugins that are made available by the server admin. Updates to all sites can be pushed at once, ensuring that they are always kept safe and secure.  
WordPress Multisite is great for organizations such as universities, corporations, and agencies that need to enable many people to host their own websites while giving overall control to a central administrator.  
[Set up WordPress Multisite on Lightsail](amazon-lightsail-quick-start-guide-wordpress-multisite.md)  
Learn more about [WordPress Multisite](https://bitnami.com/stack/wordpress-multisite) at the *Bitnami* website.

** **cPanel & WebHost Manager (WHM)** **  
cPanel & WHM is a suite of tools built for Linux OS that gives you the ability to automate web hosting tasks by using a simple graphical user interface. Its goal is to make managing servers easier for you and managing websites easier for your customers.  
[Host websites, email, and services with cPanel & WHM on Lightsail](amazon-lightsail-quick-start-guide-cpanel.md)  
Learn more about [cPanel & WHM](https://cpanel.net/products/cpanel-whm-features/) at the *cPanel* website.

** **PrestaShop packaged by Bitnami** **  
PrestaShop is one of the most prolific ecommerce solutions in the world. It is free and open source software, with a community of over 1 million active members. It is designed to get your online store up and running quickly, with a preconfigured theme so that you can start selling almost immediately along with a Live Configurator for easily customizing the look of your site. PrestaShop features multi-store support, customizable URLs, multiple payment gateway options (including PayPal and Stripe), and marketplace integration with Amazon, eBay, Facebook and more.  
[Set up a PrestaShop website on Lightsail](amazon-lightsail-quick-start-guide-prestashop.md)  
Learn more about [https://prestashop.com](https://prestashop.com) at the *PrestaShop* website.

** **Ghost packaged by Bitnami** **  
Ghost is a publishing platform that is suitable for everything from personal blogs to major news websites. Built on Node.js, its modern technology stack makes it versatile and flexible for developers seeking to integrate with other applications and tools, while maintaining ease of use for content creators.  
[Deploy a Ghost website on Lightsail](amazon-lightsail-quick-start-guide-ghost.md)  
Learn more about [Bitnami Ghost](https://bitnami.com/stack/ghost) at the *Bitnami* website.

** **Joomla\! packaged by Bitnami** **  
Bitnami Joomla\! is a preconfigured, ready-to-use image for running Joomla\! on Lightsail. Joomla\! is a CMS that you can use to build a variety of websites or portals. These include personal, corporate, small business, nonprofit, and other organizational websites.  
Joomla\! also features a registration system that enables users to configure personal options. Authentication is an important part of user management, and Joomla\! supports multiple protocols, including LDAP, OpenID, and others. Joomla\! supports many different languages and offers guidance for using them for the website and the administration panel. Also, the **Banner Manager** makes it easy to set up and manage banners on your site. You can track metrics, including setting impression numbers, special URLs, and more.   
[Get started with Joomla\! on Lightsail](amazon-lightsail-quick-start-guide-joomla.md)  
Learn more about [Joomla\!](https://bitnami.com/stack/joomla) at the *Bitnami* website.

** **Drupal packaged by Bitnami** **  
Bitnami Drupal is a preconfigured, ready-to-use image for running Drupal on Lightsail. Drupal is a content management platform that helps users easily publish, manage, and organize content. It's used for community web portals, discussion sites, corporate websites, and more. You can easily extend Drupal by plugging in modules. Drupal is built for high performance, is scalable to many servers, and has easy integration with REST, JSON, SOAP, and other formats.  
There are thousands of add-on modules and designs available for Drupal free of charge. Drupal is also available in multiple languages.  
[Set up and customize your Drupal website on Lightsail](amazon-lightsail-quick-start-guide-drupal.md)  
Learn more about [Drupal](https://bitnami.com/stack/drupal) at the *Bitnami* website.

## Application stacks and servers
<a name="compare-application-stacks-servers"></a>

Lightsail has multiple application stacks and servers for a wide variety of development projects. Each image uses Linux/Unix as the base operating system.

** **OpenClaw** **  
OpenClaw is an open-source autonomous AI agent (formerly Clawdbot/Moltbot). It runs continuously in the background on your own server, connecting to messaging platforms like Slack, Telegram, WhatsApp, and Discord as its primary interface. OpenClaw features proactive task execution, multi-channel integration, and the ability to run code, manage files, and browse the web.  
Lightsail instances launched from OpenClaw will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
[Get started with OpenClaw on Lightsail](amazon-lightsail-quick-start-guide-openclaw.md)  
Learn more about [OpenClaw](https://openclaw.ai) at the *OpenClaw* website.

** **LAMP stack (PHP 8) packaged by Bitnami** **  
The Bitnami LAMP stack simplifies the development and deployment of PHP applications. It includes ready-to-run versions of Apache, MySQL, PHP, and phpMyAdmin, and also the other software required to run each of those components. Bitnami LAMP stack is completely integrated and configured, so you will be ready to start developing your application as soon as you create your instance in Lightsail. Bitnami LAMP stack is regularly updated to ensure that you always have access to the latest stable releases for each bundled component.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
[Launch and configure a LAMP packaged by Bitnami instance](amazon-lightsail-quick-start-guide-lamp-bitnami.md)  
Learn more about the [Bitnami LAMP stack](https://bitnami.com/stack/lamp) at the *Bitnami* website.

** **LAMP** **  
 The LAMP blueprint provides a complete production environment with PHP, Apache, and MariaDB on Linux. This blueprint also includes phpMyAdmin, PHP core modules, and Composer.   
Lightsail instances launched from LAMP will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
[Launch and configure a LAMP instance](amazon-lightsail-launch-and-configure-lamp.md)

** **Django packaged by Bitnami** **  
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Python is a dynamic object-oriented programming language that can be used for many kinds of software development. The Bitnami Django Stack greatly simplifies the deployment of Django and its runtime dependencies and includes ready-to-run versions of Python, Django, MySQL, and Apache.  
Learn more about the [Bitnami Django stack](https://bitnami.com/stack/django) at the *Bitnami* website.

** **Node.js packaged by Bitnami** **  
Bitnami Node.js is a preconfigured, ready-to-use image for running Node.js on Lightsail. Node.js is a platform built on Chrome's JavaScript runtime for easily creating fast, scalable network applications. It uses an event-driven, non-blocking I/O model that makes it lightweight and efficient. Node.js is well suited for data-intensive, real-time applications.  
[Deploy and manage a Node.js stack on Lightsail](amazon-lightsail-quick-start-guide-nodejs.md)  
Learn more about the [Node.js stack](https://bitnami.com/stack/nodejs) at the *Bitnami* website.

** **Node.js** **  
 The Node.js blueprint provides a complete production environment with MariaDB and Node.js. Lightsail packages blueprints to be secure and up-to-date using industry best practices.   
Lightsail instances launched from Node.js will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
[Deploy and manage a Node.js stack on Lightsail](amazon-lightsail-quick-start-guide-nodejs.md)  
Learn more about the [Node.js stack](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) at the *Node.js* website.

** **MEAN stack packaged by Bitnami** **  
Bitnami MEAN stack provides a complete development environment for MongoDB and Node.js that you can deploy in one click. It includes the latest stable release of MongoDB, Express, Angular, Node.js, Git, PHP, and RockMongo.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
Learn more about the [MEAN stack](https://bitnami.com/stack/mean) at the *Bitnami* website.

** **GitLab CE Packaged by Bitnami** **  
Bitnami GitLab Community Edition (CE) is a preconfigured, ready-to-use image for running GitLab on Lightsail. GitLab is self-hosted Git management software that is fast, secure, and based on Ruby on Rails. GitLab CI (also included) is an open source Continuous Integration (CI) server closely integrated with Git and GitLab.  
 With GitLab, you keep your code secure on your own server, manage repositories, users, and access permissions. It's self-contained, so you can duplicate or move the installation to different servers easily.   
[Set up and configure a GitLab CE instance on Lightsail](amazon-lightsail-quick-start-guide-gitlab.md)  
Learn more about the [GitLab stack](https://bitnami.com/stack/gitlab) at the *Bitnami* website.

** **Nginx (LEMP stack) packaged by Bitnami** **  
Bitnami NGINX Stack provides a complete PHP, MySQL, and NGINX development environment that you can launch in one click. It also bundles phpMyAdmin, SQLite, ImageMagick, FastCGI, Memcache, GD, CURL, PEAR, PECL, and other components.  
 NGINX is an asynchronous server and its main advantage is scalability. The NGINX stack is also known as LEMP (Linux, NGINX, MySQL, and PHP).   
[Deploy and manage an Nginx web server on Lightsail](amazon-lightsail-quick-start-guide-nginx.md)  
Learn more about the [NGINX stack](https://bitnami.com/stack/nginx) at the *Bitnami* website.

** **Nginx** **  
 The Nginx blueprint provides a complete production environment with PHP, MariaDB, phpMyAdmin, and NGINX. Lightsail packages blueprints to be secure and up-to-date using industry best practices.   
Lightsail instances launched from Nginx will have Instance Metadata Service Version 2 (IMDSv2) enforced by default. For more information, see [How Instance Metadata Service Version 2 works](amazon-lightsail-configuring-instance-metadata-service.md).  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
[Deploy and manage an Nginx web server on Lightsail](amazon-lightsail-quick-start-guide-nginx.md)  
Learn more about the [NGINX stack](https://nginx.org/en/) at the *NGINX* website.

** **Plesk Hosting Stack on Ubuntu**, **Plesk Hosting Stack on Ubuntu (BYOL)****  
On August 1, 2024, Plesk transitioned to a paid license model. The following licensing behaviors apply to Lightsail instances running Plesk:  
+ Starting on February 1, 2025, a paid license is required for any instance that uses the older **Plesk Hosting Stack on Ubuntu** blueprint.
+ Instances launched with the **Plesk Hosting Stack on Ubuntu (BYOL)** blueprint have a 30-day trial license. After 30 days, you must purchase a license from Plesk to continue using the Plesk application.
For more information, see [Purchase a Plesk license](https://docs.aws.amazon.com/lightsail/latest/userguide/set-up-and-configure-plesk-stack-on-lightsail.html#amazon-lightsail-purchase-plesk-license).
Build, secure, and run websites and applications on Lightsail and AWS using the Hosting Stack powered by Plesk. This includes all your web-based server management and security tools, plus WordPress automation in a graphical user interface. It simplifies the work of web professionals and provides the scalability, security, and performance that your customers need.  
 [Set up and configure Plesk](set-up-and-configure-plesk-stack-on-lightsail.md).   
Learn more about the [Plesk stack](https://docs.plesk.com/en-US/current/administrator-guide/about-plesk.70559/) at the *Plesk* website.

** **Ruby on Rails** **  
The Ruby on Rails blueprint comes pre-configured with Rails on Amazon Linux 2023, eliminating the need for manual framework installation and setup. The Ruby on Rails blueprint enables you to deploy a robust, scalable, and cost-effective solution for building modern web applications on Lightsail.  
[Set up Ruby on Rails on Lightsail](amazon-lightsail-quick-start-guide-rubyonrails.md)  
Learn more about [Ruby on Rails](https://guides.rubyonrails.org/getting_started.html) and [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/).

## Ecommerce applications
<a name="compare-ecommerce-applications-in-lightsail"></a>

Lightsail currently has one ecommerce application image: Magento. This Magento image uses Linux/Unix (Ubuntu) as the base operating system.

 **Magento packaged by Bitnami**   
Bitnami Magento is a preconfigured, ready-to-use image for running Magento on Lightsail. You can build engaging, responsive, and secure sites using Magento. Magento is a feature-rich, flexible ecommerce solution that includes transaction options, multistore functionality, loyalty programs, product categorization, shopper filtering, promotion rules, and more.  
You can use Magento to create a highly customized ecommerce site that reflects your brand. Magento integrates with your business operations, so you can manage your ecommerce site as your business needs.   
[Set up and configure Magento on Lightsail](amazon-lightsail-quick-start-guide-magento.md)  
Learn more about the [Magento stack](https://bitnami.com/stack/magento) at the *Bitnami* website.

## Project management applications
<a name="compare-project-management-applications-in-lightsail"></a>

Lightsail currently has one project management application image, Redmine. This image uses Linux/Unix (Ubuntu) as the base operating system.

 **Redmine packaged by Bitnami**   
Bitnami Redmine is a preconfigured, ready-to-use image for running Redmine on Lightsail. Redmine is a flexible project management web application. It includes support for multiple projects, role-based access control, Gantt charts and calendars, management of news, documents, and files, per-project wikis and forums, SCM integration, and more.  
This blueprint is compatible with both dual-stack and IPv6-only Lightsail instance plans.  
[Configure and secure a Redmine instance on Lightsail](amazon-lightsail-quick-start-guide-redmine.md)  
Learn more about the [Redmine stack](https://bitnami.com/stack/redmine) at the *Bitnami* website.