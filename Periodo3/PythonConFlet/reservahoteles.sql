-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-08-2024 a las 06:38:36
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `reservahoteles`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_personales`
--

CREATE TABLE `datos_personales` (
  `id_datos` int(11) NOT NULL,
  `nombres` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_personales`
--

INSERT INTO `datos_personales` (`id_datos`, `nombres`, `apellidos`, `correo`, `edad`, `telefono`, `direccion`, `id_usuario`) VALUES
(1, 'Ulises Andrés', 'Guzmán Mejía', 'ulises@example.com', 16, '61439068', 'Tu dirección aquí', 1),
(2, 'Juan', 'Pérez', NULL, 20, '00000000', 'Dirección de Juan Pérez', 2),
(3, 'Ulises', 'Mejia', 'ulises0012@gmail.com', 18, '12121212', 'fghj', 3),
(4, 'Carlos Adrían', 'Alvizurez', 'carlitos@gmail.com', 18, '11111111', 'wsedrftgbhnjk', 4),
(5, 'Diego', 'Villacorta', 'dsvillacorta@gmail.com', 17, '+503 7092-6785', 'San Salvador', 5),
(6, 'Diego Sebastian', 'Villacorta Villalobos', 'dsvillacorta@gmail.com', 18, '(+503) 7092 6785', 'San Salvador, El Salvador', 6),
(7, 'Juanito', 'Dubon', 'dfghj@gmail.com', 11, '12121212', 'xvbfgnhmj,k.l-', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitaciones`
--

CREATE TABLE `habitaciones` (
  `id_habitacion` int(11) NOT NULL,
  `id_hotel` int(11) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `num_habi` varchar(11) NOT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `capacidad_adultos` int(11) DEFAULT NULL,
  `capacidad_ninos` int(11) DEFAULT NULL,
  `disponible` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `habitaciones`
--

INSERT INTO `habitaciones` (`id_habitacion`, `id_hotel`, `tipo`, `num_habi`, `precio`, `capacidad_adultos`, `capacidad_ninos`, `disponible`) VALUES
(1, 1, 'Doble', 'RD103', 200.00, 2, 1, 1),
(2, 1, 'Suite', 'RS103', 300.00, 2, 1, 1),
(3, 1, 'Suite', 'RS104', 300.00, 2, 1, 1),
(4, 1, 'Individual', 'RI105', 150.00, 1, 0, 1),
(5, 2, 'Suite', 'RS1001', 400.00, 2, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hoteles`
--

CREATE TABLE `hoteles` (
  `hotel_id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `imagen` blob DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `hoteles`
--

INSERT INTO `hoteles` (`hotel_id`, `nombre`, `ubicacion`, `categoria`, `imagen`, `correo`, `telefono`) VALUES
(1, 'Hotel Real InterContinental', 'Boulevard De Los Heroes, Y Avenue Sisimiles, San Salvador', '4 estrellas', , 'intercontinental@gamil.com', '2211 3333'),
(2, 'Hotel Sheraton Presidente', 'Avenida De La Revolucion, San Salvador', '4 estrellas', , 'presidente@gmail.com', '2283 4000');
INSERT INTO `hoteles` (`hotel_id`, `nombre`, `ubicacion`, `categoria`, `imagen`, `correo`, `telefono`) VALUES
(3, 'Hotel Barceló', 'Bulevar Del Hipodromo, San Salvador', '4 estrellas', , 'Barcelo@gmail.com', '2268 4545');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `id_reserva` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `fecha_entrada` date DEFAULT NULL,
  `fecha_salida` date DEFAULT NULL,
  `num_adultos` int(11) DEFAULT NULL,
  `num_ninos` int(11) DEFAULT NULL,
  `precio_total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`id_reserva`, `id_usuario`, `fecha_entrada`, `fecha_salida`, `num_adultos`, `num_ninos`, `precio_total`) VALUES
(2, 2, '2024-03-08', '2024-03-09', 2, 0, 200.00),
(4, 1, '2024-03-19', '2024-03-30', 1, 0, 2200.00),
(5, 1, '2024-04-01', '2024-04-10', 1, 0, 1800.00),
(6, 1, '2024-03-06', '2024-03-07', 2, 2, 200.00),
(7, 2, '2024-03-22', '2024-03-23', 1, 1, 200.00),
(8, 2, '2024-05-01', '2024-05-09', 2, 1, 1600.00),
(9, 4, '2024-05-15', '2024-05-24', 2, 0, 1800.00),
(10, 1, '2024-08-01', '2024-08-02', 1, 1, 200.00),
(11, 1, '2024-03-06', '2024-03-07', 1, 0, 300.00),
(12, 2, '2024-03-01', '2024-03-02', 1, 0, 150.00),
(13, 1, '2024-03-01', '2024-03-02', 1, 1, 300.00),
(14, 1, '2024-03-14', '2024-03-15', 1, 1, 300.00),
(15, 1, '2024-03-23', '2024-03-30', 1, 1, 2100.00),
(16, 1, '2024-03-06', '2024-03-07', 1, 0, 300.00),
(17, 1, '2024-03-06', '2024-03-07', 1, 0, 300.00),
(18, 1, '2024-03-01', '2024-03-03', 1, 0, 600.00),
(19, 5, '2024-04-05', '2024-04-08', 1, 1, 600.00),
(20, 1, '2024-03-01', '2024-03-02', 2, 0, 200.00),
(21, 1, '2024-04-17', '2024-04-19', 2, 1, 400.00),
(22, 4, '2024-01-09', '2024-01-11', 1, 0, 300.00),
(23, 4, '2024-03-14', '2024-03-15', 1, 0, 300.00),
(24, 1, '2024-01-11', '2024-01-12', 1, 0, 200.00),
(25, 7, '2024-01-01', '2024-01-08', 1, 0, 1050.00),
(26, 1, '2024-09-01', '2024-09-12', 2, 1, 2200.00),
(27, 4, '2024-03-20', '2024-03-21', 0, 0, 200.00),
(28, 3, '2024-03-01', '2024-03-09', 2, 1, 2400.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas_habitaciones`
--

CREATE TABLE `reservas_habitaciones` (
  `id_reserva` int(11) NOT NULL,
  `id_habitacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservas_habitaciones`
--

INSERT INTO `reservas_habitaciones` (`id_reserva`, `id_habitacion`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 2),
(12, 4),
(13, 2),
(14, 2),
(15, 2),
(16, 2),
(17, 3),
(18, 3),
(19, 1),
(20, 1),
(21, 1),
(22, 4),
(23, 3),
(24, 1),
(25, 4),
(26, 1),
(27, 1),
(28, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `nombre_rol` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `nombre_rol`) VALUES
(1, 'admin'),
(2, 'usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `contrasena` varchar(250) DEFAULT NULL,
  `id_rol` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `usuario`, `contrasena`, `id_rol`) VALUES
(1, 'admin', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 1),
(2, 'juanperez', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(3, 'Ulis3s0012', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(4, 'CardrianS', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(5, 'dsvillalobosss', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2),
(6, 'dsvillalobosss', '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5', 2),
(7, 'Juanito', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos_personales`
--
ALTER TABLE `datos_personales`
  ADD PRIMARY KEY (`id_datos`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`id_habitacion`),
  ADD KEY `id_hotel` (`id_hotel`);

--
-- Indices de la tabla `hoteles`
--
ALTER TABLE `hoteles`
  ADD PRIMARY KEY (`hotel_id`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`id_reserva`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `reservas_habitaciones`
--
ALTER TABLE `reservas_habitaciones`
  ADD PRIMARY KEY (`id_reserva`,`id_habitacion`),
  ADD KEY `id_habitacion` (`id_habitacion`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos_personales`
--
ALTER TABLE `datos_personales`
  MODIFY `id_datos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  MODIFY `id_habitacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `hoteles`
--
ALTER TABLE `hoteles`
  MODIFY `hotel_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `datos_personales`
--
ALTER TABLE `datos_personales`
  ADD CONSTRAINT `datos_personales_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD CONSTRAINT `fk_hotel_habitacion` FOREIGN KEY (`id_hotel`) REFERENCES `hoteles` (`hotel_id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `reservas_habitaciones`
--
ALTER TABLE `reservas_habitaciones`
  ADD CONSTRAINT `reservas_habitaciones_ibfk_1` FOREIGN KEY (`id_habitacion`) REFERENCES `habitaciones` (`id_habitacion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
