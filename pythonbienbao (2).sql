-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 12, 2024 lúc 06:41 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `pythonbienbao`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `hoten` varchar(255) NOT NULL,
  `vip` tinyint(1) NOT NULL DEFAULT 0,
  `soluotquettrongngay` int(11) NOT NULL,
  `tongluotquet` int(11) NOT NULL,
  `soluothailong` int(10) NOT NULL DEFAULT 0,
  `soluotkhonghailong` int(10) NOT NULL,
  `sotiennap` int(10) NOT NULL,
  `trangthai` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `password`, `email`, `hoten`, `vip`, `soluotquettrongngay`, `tongluotquet`, `soluothailong`, `soluotkhonghailong`, `sotiennap`, `trangthai`) VALUES
(5, 'helo2', '$2b$12$A89YVMJaUAQt6zX/z4r/uOU5URf.2EQ6EfKypKy0xDaK53Ev.un8e', 'helo2@gmail.com', '', 0, 0, 0, 0, 0, 0, 0),
(7, 'huy', '$2b$12$ZBmk8h3KcT8Z3EEjo1x85.gdTth.o9dZZvSA7uAjLpnqvtP2.wtnG', 'huy@gmail.com', '', 0, 0, 0, 0, 0, 0, 0),
(8, 'huy1', '$2b$12$TUqV6nv8Xo46.kp0ujU29eLZ3DLZ7qTQ9/w.5GnT3LNJO63Ydb0c6', 'huy1@gmail.com', '', 0, 0, 0, 0, 0, 0, 0),
(9, 'huy2', '$2b$12$Bc./8SakAK5I0g5yATaVy.pGmaXGM8W5mQMrhaGAfadBN9MnwZXHK', 'huy2@gmail.com', '', 0, 0, 0, 0, 0, 0, 0),
(10, '', '$2b$12$j1dI3kgxsEoqzRiMBoqZ0.ExccqCEG84sHvVezGg.seu6gsCGeznC', '', '', 0, 0, 0, 0, 0, 0, 0),
(11, 'huy123', '$2b$12$6Nx0aIiSvPG0ma4SABUIuOOrxNkBtU3ZPE7EDgPu.nFFyEeWEEj7G', 'quochuy@gmail.com', 'Nguyễn Quốc Huy', 1, 8, 13, 5, 0, 0, 0),
(12, '123', '$2b$12$GQm2HPExJS3tb4q2g30CrOuxekKVIB8OZGKQxslk8xIpSDFNaEr12', '123', '', 0, 0, 0, 0, 0, 0, 0),
(13, '123123', '$2b$12$jZDfDgGkVRaR0ej.xh6ZHeimaG3rWQnGaF9.KneoR0uyKD9nxuYQ2', '123123', '', 0, 0, 0, 0, 0, 0, 0),
(14, '1', '$2b$12$nhXFyf7AfVXIeVa/9M.Kc.AcGAqMxMmAVwWii9EU0BL.QtB7JhDZe', '', '', 0, 0, 0, 0, 0, 0, 0),
(15, '123456', '$2b$12$DddJchA09AY8jBlFL9u/bus8.14pNfDJyORzbL1YOh53/0wELuKj6', '123456', '', 0, 0, 0, 0, 0, 0, 0),
(17, 'quochuy3792@gmail.com', '', 'quochuy3792@gmail.com', 'Nguyễn Quốc Huy', 0, 2, 2, 0, 0, 0, 0),
(18, 'quochuyforgame@gmail.com', '', 'quochuyforgame@gmail.com', 'Nguyễn Quốc Huy', 0, 0, 0, 0, 0, 0, 0),
(19, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(20, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(21, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(22, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(23, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(24, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(25, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(26, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(27, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(28, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(29, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(30, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(31, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(32, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(33, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(34, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(35, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(36, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0),
(37, '[value-2]', '[value-3]', '[value-4]', '[value-5]', 0, 0, 0, 0, 0, 0, 0);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
