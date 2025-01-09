BEGIN TRANSACTION
--
-- Create model Person
--
CREATE TABLE [person] ([id] int NOT NULL PRIMARY KEY IDENTITY (1, 1), [name] nvarchar(150) NOT NULL, [birthdate] date NULL);
--
-- Create model Movie
--
CREATE TABLE [movie] ([id] int NOT NULL PRIMARY KEY IDENTITY (1, 1), [title] nvarchar(300) NOT NULL, [year] int NOT NULL, [duration] int NULL, [synopsis] nvarchar(max) NULL, [color] nvarchar(20) NULL, [poster_uri] nvarchar(15) NULL, [director_id] int NULL);
CREATE TABLE [play] ([id] bigint NOT NULL PRIMARY KEY IDENTITY (1, 1), [movie_id] int NOT NULL, [person_id] int NOT NULL);
ALTER TABLE [movie] ADD CONSTRAINT [movie_director_id_a1a23574_fk_person_id] FOREIGN KEY ([director_id]) REFERENCES [person] ([id]);
CREATE UNIQUE INDEX [play_movie_id_person_id_0c405d42_uniq] ON [play] ([movie_id], [person_id]) WHERE [movie_id] IS NOT NULL AND [person_id] IS NOT NULL;
ALTER TABLE [play] ADD CONSTRAINT [play_person_id_23ae9fa8_fk_person_id] FOREIGN KEY ([person_id]) REFERENCES [person] ([id]);
CREATE INDEX [play_movie_id_b073e9b8] ON [play] ([movie_id]);
ALTER TABLE [play] ADD CONSTRAINT [play_movie_id_b073e9b8_fk_movie_id] FOREIGN KEY ([movie_id]) REFERENCES [movie] ([id]);
CREATE INDEX [movie_director_id_a1a23574] ON [movie] ([director_id]);
CREATE INDEX [play_person_id_23ae9fa8] ON [play] ([person_id]);
COMMIT;
