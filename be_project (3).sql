-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2019 at 11:33 AM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `be_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `Emp_id` int(11) NOT NULL,
  `Team_id` int(11) DEFAULT NULL,
  `Full_name` text NOT NULL,
  `Designation` text NOT NULL,
  `Email_id` text NOT NULL,
  `Dob` date NOT NULL,
  `ip_address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`Emp_id`, `Team_id`, `Full_name`, `Designation`, `Email_id`, `Dob`, `ip_address`) VALUES
(1, 1, 'Navina Sinari', 'Socket Programmer', 'navinasinari@gmail.com', '1997-01-17', '172.31.4.70'),
(2, 1, 'Pranav Silimkhan', 'Socket Programmer/Leader', 'pranavsilimkhan@gmail.com', '1997-10-04', '172.31.4.72'),
(3, 1, 'Nandan Prabhudesai', 'Ui designer', 'nandanprabhudesai@gmail.com', '1997-03-25', '192.168.43.190'),
(4, 1, 'Anay Naik', 'Ui designer', 'anaynaik@gmail.com', '1996-12-28', '192.168.43.111'),
(6, 3, 'Ramesh yadav', 'debugger', 'ramesh@gmail.com', '1996-01-25', '0'),
(7, 1, 'Anag gaunekar', 'coder', 'anag@gmail.com', '1997-05-08', '0');

-- --------------------------------------------------------

--
-- Stand-in structure for view `group_chat`
-- (See below for the actual view)
--
CREATE TABLE `group_chat` (
`sender_id` int(11)
,`sender_name` text
,`group_id` int(11)
,`group_name` text
,`message_body` text
,`message_type` text
,`time` timestamp
);

-- --------------------------------------------------------

--
-- Table structure for table `group_members`
--

CREATE TABLE `group_members` (
  `Group_id` int(11) NOT NULL,
  `Member_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `group_members`
--

INSERT INTO `group_members` (`Group_id`, `Member_id`) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 1),
(3, 2),
(3, 3),
(3, 4);

-- --------------------------------------------------------

--
-- Stand-in structure for view `group_member_name`
-- (See below for the actual view)
--
CREATE TABLE `group_member_name` (
`Employee_id` int(11)
,`Emp_name` text
,`Group_Name` text
,`Group_id` int(11)
);

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `Message_ID` int(11) NOT NULL,
  `Message_body` text NOT NULL,
  `Sender_id` int(11) DEFAULT NULL,
  `Receiver_Id` int(11) DEFAULT NULL,
  `Receiver_group_id` int(11) DEFAULT NULL,
  `message_type` text NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`Message_ID`, `Message_body`, `Sender_id`, `Receiver_Id`, `Receiver_group_id`, `message_type`, `time`) VALUES
(13, 'hello', 4, 2, NULL, 'personal', '2019-04-03 09:26:32'),
(14, 'hiii', 4, 2, NULL, 'personal', '2019-04-03 09:26:32'),
(15, 'dgdge', 4, 2, NULL, 'personal', '2019-04-03 09:26:32'),
(16, 'hey', 3, 2, NULL, 'personal', '2019-04-03 09:26:32'),
(17, 'bro', 4, 2, NULL, 'personal', '2019-04-03 09:26:32'),
(18, 'chats is working', 3, 2, NULL, 'personal', '2019-04-03 09:26:32'),
(19, 'sup', 4, 2, NULL, 'personal', '2019-04-03 09:26:32'),
(20, 'array bro', 3, 2, NULL, 'personal', '2019-04-03 10:34:05'),
(21, 'bububuub', 4, 2, NULL, 'personal', '2019-04-03 10:34:06'),
(22, 'adi amhi chappati khatale', 3, 2, NULL, 'personal', '2019-04-03 10:34:11'),
(23, 'hi', 4, 2, NULL, 'personal', '2019-04-03 10:51:00'),
(24, 'uooo', 4, 2, NULL, 'personal', '2019-04-03 10:51:07'),
(25, 'j', 4, 2, NULL, 'personal', '2019-04-03 10:51:11'),
(26, 'uuu', 4, 2, NULL, 'personal', '2019-04-03 10:51:13'),
(27, 'hello', 4, 2, NULL, 'personal', '2019-04-03 11:00:27'),
(28, 'h', 4, 2, NULL, 'personal', '2019-04-03 11:00:39'),
(29, 'ff', 4, 2, NULL, 'personal', '2019-04-03 11:00:43'),
(30, 'rrr', 4, 2, NULL, 'personal', '2019-04-03 11:00:46'),
(31, 'rrrrr', 4, 2, NULL, 'personal', '2019-04-03 11:00:49'),
(32, 'etet', 4, 2, NULL, 'personal', '2019-04-03 11:00:56');

-- --------------------------------------------------------

--
-- Table structure for table `message_group`
--

CREATE TABLE `message_group` (
  `Group_id` int(11) NOT NULL,
  `Group_Name` text NOT NULL,
  `Group_Admin_Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `message_group`
--

INSERT INTO `message_group` (`Group_id`, `Group_Name`, `Group_Admin_Id`) VALUES
(1, 'Socket_programmers', 2),
(2, 'Ui_Designers', 3),
(3, 'Be_Project', 2);

-- --------------------------------------------------------

--
-- Table structure for table `notices`
--

CREATE TABLE `notices` (
  `Notice_id` int(11) NOT NULL,
  `leader_id` int(11) NOT NULL,
  `notice_body` text NOT NULL,
  `date_created` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `notices`
--

INSERT INTO `notices` (`Notice_id`, `leader_id`, `notice_body`, `date_created`) VALUES
(1, 2, 'Review on 22nd March', '2019-03-19');

-- --------------------------------------------------------

--
-- Stand-in structure for view `personal_chat`
-- (See below for the actual view)
--
CREATE TABLE `personal_chat` (
`sender_id` int(11)
,`sender_name` text
,`receiver_id` int(11)
,`Receiver_name` text
,`message_body` text
,`message_type` text
,`time` timestamp
);

-- --------------------------------------------------------

--
-- Table structure for table `ports`
--

CREATE TABLE `ports` (
  `Sr_no` int(11) NOT NULL,
  `Port_no` int(11) NOT NULL,
  `Status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `Team_id` int(11) NOT NULL,
  `Team_name` text NOT NULL,
  `Leader_Id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`Team_id`, `Team_name`, `Leader_Id`) VALUES
(1, 'Coders', 2),
(3, 'debuggers', 6);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Emp_id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `user_type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Emp_id`, `username`, `password`, `user_type`) VALUES
(1, 'navinasinari', '5f4dcc3b5aa765d61d8327deb882cf99', 'standard'),
(2, 'pranavsilimkhan', '5f4dcc3b5aa765d61d8327deb882cf99', 'admin'),
(3, 'nandan', '83878c91171338902e0fe0fb97a8c47a', 'standard'),
(4, 'anaynaik', '5f4dcc3b5aa765d61d8327deb882cf99', 'standard'),
(7, 'anag', '5f4dcc3b5aa765d61d8327deb882cf99', 'standard');

-- --------------------------------------------------------

--
-- Table structure for table `video_message`
--

CREATE TABLE `video_message` (
  `Video_id` int(11) NOT NULL,
  `Video` longblob NOT NULL,
  `Leader_Id` int(11) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `video_message`
--

INSERT INTO `video_message` (`Video_id`, `Video`, `Leader_Id`, `time`) VALUES
(1, 0x6d6573736167652067726f75700d0a67726f75705f6964202067726f75705f6e616d65202067726f75705f61646d696e5f69640d0a67726f75705f6d656d626572730d0a47726f75705f6964204d656d6265725f69640d0a6d6573736167650d0a6d6573736167655f6964206d6573736167655f626f64792053656e6465725f69642052656365697665725f6964206d6573736167655f747970652074696d650d0a75736572730d0a456d705f696420757365726e616d652070617373776f726420757365725f747970650d0a656d706c6f7965650d0a456d705f6964205465616d5f69642046756c6c5f4e616d652044657369676e6174696f6e20456d61696c2d696420444f4220656d705f747970650d0a5465616d730d0a5465616d5f696420205465616d5f6e616d65204c65616465725f6964, 2, '2019-02-05 01:00:09');

-- --------------------------------------------------------

--
-- Structure for view `group_chat`
--
DROP TABLE IF EXISTS `group_chat`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `group_chat`  AS  select `sender`.`Emp_id` AS `sender_id`,`sender`.`Full_name` AS `sender_name`,`receiver`.`Group_id` AS `group_id`,`receiver`.`Group_Name` AS `group_name`,`message`.`Message_body` AS `message_body`,`message`.`message_type` AS `message_type`,`message`.`time` AS `time` from ((`message` join `employee` `sender` on((`message`.`Sender_id` = `sender`.`Emp_id`))) join `message_group` `receiver` on((`message`.`Receiver_group_id` = `receiver`.`Group_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `group_member_name`
--
DROP TABLE IF EXISTS `group_member_name`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `group_member_name`  AS  select `employee`.`Emp_id` AS `Employee_id`,`employee`.`Full_name` AS `Emp_name`,`message_group`.`Group_Name` AS `Group_Name`,`group_members`.`Group_id` AS `Group_id` from ((`employee` join `group_members` on((`group_members`.`Member_id` = `employee`.`Emp_id`))) join `message_group` on((`message_group`.`Group_id` = `group_members`.`Group_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `personal_chat`
--
DROP TABLE IF EXISTS `personal_chat`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `personal_chat`  AS  select `sender`.`Emp_id` AS `sender_id`,`sender`.`Full_name` AS `sender_name`,`receiver`.`Emp_id` AS `receiver_id`,`receiver`.`Full_name` AS `Receiver_name`,`message`.`Message_body` AS `message_body`,`message`.`message_type` AS `message_type`,`message`.`time` AS `time` from ((`message` join `employee` `sender` on((`message`.`Sender_id` = `sender`.`Emp_id`))) join `employee` `receiver` on((`message`.`Receiver_Id` = `receiver`.`Emp_id`))) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`Emp_id`),
  ADD KEY `Team_id` (`Team_id`);

--
-- Indexes for table `group_members`
--
ALTER TABLE `group_members`
  ADD PRIMARY KEY (`Group_id`,`Member_id`),
  ADD KEY `Member_id` (`Member_id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`Message_ID`),
  ADD KEY `Sender_id` (`Sender_id`),
  ADD KEY `Receiver_Id` (`Receiver_Id`),
  ADD KEY `Receiver_group_id` (`Receiver_group_id`);

--
-- Indexes for table `message_group`
--
ALTER TABLE `message_group`
  ADD PRIMARY KEY (`Group_id`),
  ADD KEY `Group_Admin_Id` (`Group_Admin_Id`);

--
-- Indexes for table `notices`
--
ALTER TABLE `notices`
  ADD PRIMARY KEY (`Notice_id`),
  ADD KEY `leader_id` (`leader_id`);

--
-- Indexes for table `ports`
--
ALTER TABLE `ports`
  ADD PRIMARY KEY (`Sr_no`);

--
-- Indexes for table `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`Team_id`),
  ADD KEY `Leader_Id` (`Leader_Id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Emp_id`);

--
-- Indexes for table `video_message`
--
ALTER TABLE `video_message`
  ADD PRIMARY KEY (`Video_id`),
  ADD KEY `Leader_Id` (`Leader_Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `Emp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `Message_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `message_group`
--
ALTER TABLE `message_group`
  MODIFY `Group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `notices`
--
ALTER TABLE `notices`
  MODIFY `Notice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ports`
--
ALTER TABLE `ports`
  MODIFY `Sr_no` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `teams`
--
ALTER TABLE `teams`
  MODIFY `Team_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `video_message`
--
ALTER TABLE `video_message`
  MODIFY `Video_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Team_id`) REFERENCES `teams` (`Team_id`);

--
-- Constraints for table `group_members`
--
ALTER TABLE `group_members`
  ADD CONSTRAINT `group_members_ibfk_1` FOREIGN KEY (`Group_id`) REFERENCES `message_group` (`Group_id`),
  ADD CONSTRAINT `group_members_ibfk_2` FOREIGN KEY (`Member_id`) REFERENCES `employee` (`Emp_id`);

--
-- Constraints for table `message`
--
ALTER TABLE `message`
  ADD CONSTRAINT `message_ibfk_1` FOREIGN KEY (`Sender_id`) REFERENCES `employee` (`Emp_id`),
  ADD CONSTRAINT `message_ibfk_2` FOREIGN KEY (`Receiver_Id`) REFERENCES `employee` (`Emp_id`),
  ADD CONSTRAINT `message_ibfk_3` FOREIGN KEY (`Receiver_group_id`) REFERENCES `message_group` (`Group_id`);

--
-- Constraints for table `message_group`
--
ALTER TABLE `message_group`
  ADD CONSTRAINT `message_group_ibfk_1` FOREIGN KEY (`Group_Admin_Id`) REFERENCES `employee` (`Emp_id`);

--
-- Constraints for table `notices`
--
ALTER TABLE `notices`
  ADD CONSTRAINT `notices_ibfk_1` FOREIGN KEY (`leader_id`) REFERENCES `employee` (`Emp_id`);

--
-- Constraints for table `teams`
--
ALTER TABLE `teams`
  ADD CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`Leader_Id`) REFERENCES `employee` (`Emp_id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`Emp_id`) REFERENCES `employee` (`Emp_id`);

--
-- Constraints for table `video_message`
--
ALTER TABLE `video_message`
  ADD CONSTRAINT `video_message_ibfk_1` FOREIGN KEY (`Leader_Id`) REFERENCES `teams` (`Leader_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
