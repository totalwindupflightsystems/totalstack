---
id: "@specs/aws/lightsail/docs/create-and-attach-additional-block-storage-disks-linux-unix"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Attach disks to Linux instances"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Attach disks to Linux instances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/create-and-attach-additional-block-storage-disks-linux-unix
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create and attach Lightsail block storage disks to Linux instances
<a name="create-and-attach-additional-block-storage-disks-linux-unix"></a>

You can create and attach additional block storage disks for your Amazon Lightsail instances. After you create additional disks, you need to connect to your Linux/Unix-based Lightsail instance and format and mount the disk.

This topic shows you how to create a new disk and attach it using Lightsail. It also describes how to connect to your Linux/Unix-based instance using SSH, so that you can format and mount your attached disk.

If you have a Windows Server-based instance, see the following topic instead: [Create and attach block storage disks to your Windows Server instance](create-and-attach-additional-block-storage-disks-windows.md).

## Step 1: Create a new disk and attach it to your instance
<a name="create-attach-new-disk-to-linux-unix-instance"></a>

1. In the left navigation pane, choose **Storage**.

1. Choose **Create disk**.

1. Choose the AWS Region and Availability Zone where your Lightsail instance is located.

1. Choose a size.

1. Enter a name for your disk.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. Choose one of the following options to add tags to your disk:
   + **Add key-only tags** or **Manage tags** (if tags have already been added). Enter your new tag into the tag key text box, and press **Enter**. Choose **Save** when you’re done entering your tags to add them, or choose **Cancel** to not add them.  
![Key-only tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-only-tags.png)
   + **Create a key-value tag**, then enter a key into the **Key** text box, and a value into the **Value** text box. Choose **Save** when you’re done entering your tags, or choose **Cancel** to not add them.

     Key-value tags can only be added one at a time before saving. To add more than one key-value tag, repeat the previous steps.  
![Key-value tags in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-key-value-tag.png)
**Note**  
For more information about key-only and key-value tags, see [Tags](amazon-lightsail-tags.md).

1. Choose **Create disk**.

   After a few seconds, your disk is created and you're on the new disk management page.

1. Choose your instance from the list, and then choose **Attach** to attach the new disk to your instance.

## Step 2: Connect to your instance to format and mount the disk
<a name="connect-to-linux-unix-instance-using-ssh-format-mount-disk"></a>

1. After you create and attach your disk, go back to the instance management page in Lightsail.

   The **Connect** tab is displayed by default.  
![The Connect tab of the instance management page](http://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-instance-management-page-connect-tab.png)

1. Choose **Connect using SSH** to connect to your instance.

1. Enter the following command into the terminal window:

   ```
   lsblk
   ```

   The output of `lsblk` omits the `/dev/` prefix from disk paths.
**Note**  
On June 29, 2023 we updated the underlying hardware for Lightsail instances. In the following examples, device names for previous generation instances are displayed as `/dev/xvda`. Device names for instances created after this date are displayed as `/dev/nvme0n1`.

------
#### [ Current generation instances ]

   In the following example output, the root volume (`nvme0n1`) has two partitions (`nvme0n1p1` and `nvme0n1p128`), while the additional volume (`nvme1n1`) has no partitions.

   ```
   [ec2-user ~]$ sudo lsblk
   NAME          MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
   nvme1n1       259:0    0  30G  0 disk /data
   nvme0n1       259:1    0  16G  0 disk
   └─nvme0n1p1   259:2    0   8G  0 part /
   └─nvme0n1p128 259:3    0   1M  0 part
   ```

------
#### [ Previous generation instances ]

   In the following example output, the root volume (`xvda`) has a partition (`xvda1`), while the additional volume (`xvdf`) has no partition.

   ```
   [ec2-user ~]$ sudo lsblk                
   NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
   xvda    202:0    0  16G  0 disk
   └─xvda1 202:1    0   8G  0 part /
   xvdf    202:80   0  24G  0 disk
   ```

------

1. Determine whether to create a file system on the disk. New disks are raw block devices, and you must create a file system on them before you can mount and use them. Disks that have been restored from snapshots likely have a file system on them already. If you create a new file system on top of an existing file system, the operation overwrites your data.

   Use the following to determine if your disk has a file system or not. If your disk does not have a file system, continue to **Step 2.5**. If your disk does have a file system, skip to **Step 2.6**.

------
#### [ Current generation instances ]

   ```
   sudo file -s /dev/nvme1n1
   ```

   You should see the following output on a brand new disk.

   ```
   /dev/nvme1n1: data
   ```

   If you see output like the following, it means that your disk already has a file system.

   ```
   /dev/nvme1n1: SGI XFS filesystem data (blksz 4096, inosz 512, v2 dirs)
   ```

------
#### [ Previous generation instances ]

   ```
   sudo file -s /dev/xvdf
   ```

   You should see the following output on a brand new disk.

   ```
   /dev/xvdf: data
   ```

   If you see output like the following, it means that your disk already has a file system.

   ```
   /dev/xvda1: Linux rev 1.0 ext4 filesystem data, UUID=1701d228-e1bd-4094-a14c-12345EXAMPLE (needs journal recovery) (extents) (large files) (huge files)
   ```

------

1. Use the following command to create a new file system on the disk. Substitute the device name (such as `/dev/nvme1n1`) for {{device\_name}}. Depending on the requirements of your application or the limitations of your operating system, you can choose a different file system type, such as `ext3` or `ext4`.
**Important**  
This step assumes that you're mounting an empty disk. If you're mounting a disk that already has data on it (for example, a disk that was restored from a snapshot), don't use `mkfs` before mounting the disk. Instead, skip to **Step 2.6** and create a mount point. Otherwise, you will format the disk and delete the existing data.

------
#### [ Current generation instances ]

   ```
   sudo mkfs -t xfs {{device_name}}
   ```

   You should see output like the following.

   ```
   meta-data=/dev/nvme1n1           isize=512    agcount=16, agsize=1048576 blks
            =                       sectsz=512   attr=2, projid32bit=1
            =                       crc=1        finobt=1, sparse=1, rmapbt=0
            =                       reflink=1    bigtime=1 inobtcount=1
   data     =                       bsize=4096   blocks=16777216, imaxpct=25
            =                       sunit=1      swidth=1 blks
   naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
   log      =internal log           bsize=4096   blocks=16384, version=2
            =                       sectsz=512   sunit=1 blks, lazy-count=1
   realtime =none                   extsz=4096   blocks=0, rtextents=0
   ```

------
#### [ Previous generation instances ]

   ```
   sudo mkfs -t ext4 {{device_name}}
   ```

   You should see the following output like the following.

   ```
   mke2fs 1.42.9 (4-Feb-2014)
   Filesystem label=
   OS type: Linux
   Block size=4096 (log=2)
   Fragment size=4096 (log=2)
   Stride=0 blocks, Stripe width=0 blocks
   4194304 inodes, 16777216 blocks
   838860 blocks (5.00%) reserved for the super user
   First data block=0
   Maximum filesystem blocks=4294967296
   512 block groups
   32768 blocks per group, 32768 fragments per group
   8192 inodes per group
   Superblock backups stored on blocks:
   32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
   4096000, 7962624, 11239424
   
   Allocating group tables: done
   Writing inode tables: done
   Creating journal (32768 blocks): done
   Writing superblocks and filesystem accounting information: done
   ```

------

1. Use the following command to create a mount point directory for the disk. The mount point is where the disk is located in the file system tree and where you read files from and write files to after you mount the disk. Substitute a location for {{mount\_point}}, for an unused space such as `/data`.

   ```
   sudo mkdir {{mount_point}}
   ```

1. You can verify that the disk now has a file system on it by entering the following command.

------
#### [ Current generation instances ]

   ```
   sudo file -s /dev/nvme1n1
   ```

   Instead of `/dev/nvme1n1: data`, you will see output similar to the following.

   ```
   /dev/nvme1n1: SGI XFS filesystem data (blksz 4096, inosz 512, v2 dirs)
   ```

------
#### [ Previous generation instances ]

   ```
   sudo file -s /dev/xvdf
   ```

   Instead of `/dev/xvdf: data`, you will see output similar to the following.

   ```
   /dev/xvdf: Linux rev 1.0 ext4 filesystem data, UUID=0ee83fdf-e370-442e-ae38-12345EXAMPLE (extents) (large files) (huge files)
   ```

------

1. Finally, mount the disk by entering the following command.

   ```
   sudo mount {{device_name mount_point}}
   ```

   Review the file permissions of your new disk mount to ensure that your users and applications can write to the disk. For more information about file permissions, see [Making an Amazon EBS Volume Available for Use](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html) in the *Amazon EC2 User Guide*.

## Step 3: Mount the disk every time you reboot your instance
<a name="mount-disk-every-time-reboot-instance-linux-unix"></a>

You probably want to mount this disk every time you reboot your Lightsail instance. If you don't, this step is optional for you.

1. To mount this disk on every system reboot, add an entry for the device to the `/etc/fstab` file.

   Create a backup of your `/etc/fstab` file that you can use if you accidentally destroy or delete this file while you're editing it.

   ```
   sudo cp /etc/fstab /etc/fstab.orig
   ```

1. Open the `/etc/fstab` file using any text editor, such as vim.

   You must enter `sudo` before opening the file so that you can save changes.

1. Add a new line to the end of the file for your disk using the following format.

   ```
   device_name  mount_point  file_system_type  fs_mntops  fs_freq  fs_passno
   ```

   For example, your new line might look something like this.

------
#### [ Current generation instances ]

   ```
   /dev/nvme1n1 /data xfs defaults,nofail 0 2
   ```

------
#### [ Previous generation instances ]

   ```
   /dev/xvdf /data ext4 defaults,nofail 0 2
   ```

------

1. Save the file and exit your text editor.