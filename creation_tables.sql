-- SET search_path TO exercice12;

-- # ### Table `utilisateurs`

-- # * `id_utilisateur` : identifiant unique (clé primaire)
-- # * `nom_utilisateur` : texte, obligatoire
-- # * `email` : texte, unique
-- # * `date_inscription` : date/heure par défaut actuelle

create table utilisateurs (
	id_utilisateur int generated always as identity primary key,
	nom_utilisateur varchar(255) not null,
	email varchar(255) not null,
	date_inscription date
);

-- delete from utilisateurs;
INSERT INTO utilisateurs (nom_utilisateur, email, date_inscription) VALUES
('Alice Dupont', 'alice.dupont@example.com', '2023-01-15'),
('Bob Martin', 'bob.martin@example.com', '2023-02-20'),
('Caroline Petit', 'caroline.petit@example.com', '2023-03-10'),
('David Leroy', 'david.leroy@example.com', '2023-04-05'),
('Emma Dubois', 'emma.dubois@example.com', '2023-05-12');
select * from utilisateurs;

-- # ### Table `chansons`

-- # * `id_chanson` : identifiant unique (clé primaire)
-- # * `titre` : texte
-- # * `artiste` : texte
-- # * `album` : texte
-- # * `duree` : nombre ou texte
-- # * `genre` : texte
-- # * `annee_sortie` : entier

create table chansons (
	id_chanson int generated always as identity primary key,
	titre varchar(255),
	artiste varchar(255),
	album varchar(255),
	duree int,
	genre varchar(255),
	annee_sortie date
);
-- delete from chansons;
INSERT INTO chansons (titre, artiste, album, duree, genre, annee_sortie) VALUES
('Stairway to Heaven', 'Led Zeppelin', 'Led Zeppelin IV', 482, 'Rock', '1971-11-08'),
('Bohemian Rhapsody', 'Queen', 'A Night at the Opera', 354, 'Rock', '1975-10-31'),
('Hotel California', 'Eagles', 'Hotel California', 391, 'Rock', '1976-12-08'),
('Smoke on the Water', 'Deep Purple', 'Machine Head', 340, 'Rock', '1972-03-25'),
('Sweet Child O''Mine', 'Guns N'' Roses', 'Appetite for Destruction', 356, 'Rock', '1987-07-21');

select * from chansons;

-- # ### Table `playlists`

-- # * `id_playlist` : identifiant unique (clé primaire)
-- # * `nom_playlist` : texte
-- # * `id_utilisateur` : clé étrangère vers `utilisateurs`
-- # * `id_chanson` : clé étrangère vers `chansons`
-- # * `date_creation` : date/heure par défaut actuelle

create table playlists(
	id_playlist int generated always as identity primary key,
	nom_playlist varchar(255),
	id_utilisateur int references utilisateurs(id_utilisateur) on delete cascade,
	id_chanson int references chansons(id_chanson) on delete cascade,
	date_creation date default current_date
);

-- delete from playlists
INSERT INTO playlists (nom_playlist, id_utilisateur, id_chanson) VALUES
('Rock Classics', 1, 1),
('Queen Favorites', 1, 2),
('Guitar Hits', 1, 3),
('Hotel Vibes', 2, 1),
('80s Rock', 2, 4),
('Led Zeppelin Collection', 2, 5),
('Epic Rock Anthems', 3, 2),
('Deep Purple Nights', 3, 3),
('Sweet Rock', 3, 4),
('Rock Legends', 4, 1),
('Metal Hits', 4, 2),
('Hard Rock', 4, 5),
('Soft Rock', 5, 3),
('Classic Ballads', 5, 4),
('Rock Revival', 5, 5),
('Guitar Heroes', 1, 4),
('Stadium Rock', 2, 3),
('Power Chords', 3, 1),
('Rock Anthems', 4, 5),
('Acoustic Rock', 5, 2);
select * from playlists;