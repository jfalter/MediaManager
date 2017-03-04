import glob, os, sys

def printUsage():
        print("Media Manager Usage : ")
        print("     python MediaManager.py <movie directory> <file to output> ")
        print("          Creates a text file with a list of all of your .m4v movies in it")
        print("     python MediaManager.py <movie directory> <file to output> <movie file to compare>")
        print("         Compares your media directory to another persons to see what each is missing")
        quit()

localMovies = []
remoteMovies = []
if len(sys.argv) < 3:
    printUsage()
elif len(sys.argv) >= 3:
    print ("Starting Media Manager....")

    for file in os.listdir(sys.argv[1]):
        if file.lower().endswith((".m4v", ".mp4", ".avi")):
            localMovies.append(file);

    print("Located %d movies locally" % len(localMovies))

    output = open(sys.argv[2], 'w')
    output.truncate()
    for movie in localMovies:
        output.write("%s\n" % movie)
    output.close()

    print("Your movie data written to %s" % sys.argv[2])
    print();
if len(sys.argv) == 4:
    #f = open(sys.argv[3])
    #remoteMovies = f.readlines()
    #f.close()
    with open(sys.argv[3]) as f:
        remoteMovies = f.read().splitlines()

    localMoviesNeeded = []
    remoteMoviesNeeded = []
    output = open("MediaManagerResults.txt", 'w')
    output.truncate()
    for movie in localMovies:
        if not movie in remoteMovies:
            localMoviesNeeded.append(movie);
    for movie in remoteMovies:
        if not movie in localMovies:
            remoteMoviesNeeded.append(movie);

    if len(localMoviesNeeded) > 0:
        output.write("Your movies to share:\n")
        print("Your movies to share:")
        for movie in localMoviesNeeded:
            output.write("%s\n" % movie)
            print(movie);
        output.write("\n\n");
        print();
    else:
        print("You have no new movies to share with the remote user since last sync.\n\n")
        output.write("You have no new movies to share with the remote user since last sync.\n\n")
    if len(remoteMoviesNeeded) > 0:
        output.write("Movies you need:\n")
        print("Movies you need:")
        for movie in remoteMoviesNeeded:
            output.write("%s\n" % movie)
            print(movie);
        output.write("\n\n");
    else:
        print("Your local movie library is completely up to date.\n\n")
        print("Your local movie library is completely up to date.");
    output.close()
