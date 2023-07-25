


# Each line contains a track id, song id, artist name, and the song title, such as: TR-
# WRJSX12903CD8446<SEP>SOBSFBU12AB018DBE1<SEP>Frank Sinatra<SEP>
# Everything Happens To Me. The only part that we care about is the song title, which
# is the final piece of data in each row. Your first function should include a regular
# expression that removes all data prior to the song title.



##preprocessing: Get a massive line, strip out all but the song title



#notes: for regex's, have to "escape" special characters with a \
#ex: \'


    #step one: Either Examine from right and remove everthing left of (and including()) the first > it finds.
    #OR, Remove efterhing left of (and including) the third <SEP>

sub preprocessing_strip_to_songtitle($line){


    # my $stripped_line1 = $line.match(rx/^.*\<SEP\>(.*)/);
    if $line.match(rx/^.*\<SEP\>(.*)**3/)
        #postmatch after
        $/.postmatch
    #stripped_line = (.....);
    # .postmatch #gets everything AFTER what is matched

    return $stripped_line1;
}

# my $song_title = "TRMTMLL12903CCF6FC<SEP>SOMPNAF12AB018E40F<SEP>Angelic Upstarts<SEP>Living In Exile (Rarities)";

# my $match = $song_title.match(rx/ ^.*\<SEP\>(.*) /);

# say $match[0].Str;

# $line
# @mul


    #step 2: write regular expression(s) to remove substrings from the title that begin
        # with any of the following characters: parentheses, brackets, curly braces, forward
        # or backslashes, underscores, dashes, colons, double quotes, backquotes, plus signs,
        # equal signs, or the featuring abbreviation (feat.). Remember to remove the period
        # at the end of ‘feat.’ Make sure to properly escape special characters in your regular
        # expressions

sub preprocessing_strip_substrings($line){

    #write regex to return NOT special characters
    my$stripped_line2 = $line;
    $stripped_line2 ~~ s:g/\(.*\)//;    #~~ means "run regex and store right back into variable" #:g is global, changes everything in string
    #repeat for all
    return $stripped_line2;


}

    #step 3: Once you have removed superfluous data, we will remove punctuation and finally
        # have clean song titles. Write a regular expression to remove all punctuation, except
        # for the apostrophe (’). Punctuation that you should remove is: ? ¿ ! ¡ . ; : & $ *
        # @ % # |
        # For the characters ¿ and ¡, you should use their unicode representations \x[00BF ]
        # and \x[00A1], respectively.


sub preprocessing_strip_punctuation($line){

    my$stripped_line3 = $line;
    #same as above, find and replace
    #[\.|/,\] strip period or comma 
    #REMEMBER GLOBAL FLAG s:g
    $stripped_line3 ~~

}

    #step 4: 
        #  Finally, we want to remove non-english characters. Write a regular expression that
        # removes all characters that are not spaces, apostrophes, lowercase letters, or upper-
        # case letters. The latter two can be done using [ a..z ] and [ A..Z ]

sub preprocessing_strip_non_english($line){

    my $stripped_line1 = $line.match(rx/^.*\<SEP\>(.*)/);
    #/[a..zA..z\.\' ]/ 
    #stripped_line = (.....);
    ##<-[i]
    return stripped_line1[1].Str;

}



#PART 2:

# 1. irst, we must tokenize each song title (split it into words). We do this by splitting
# the string on whitespace, which should leave us with just the words.
sub split_title ($line){
    my @new_line = $line.split: " ", :close;
    return @lines
}

#  Because we want to quickly find the next word in a sequence for generating a song
# title, we will use a hash table, keyed with the first word in the bigram, k1. The
# value of each entry will be another hash, keyed with the second word in the bigram
# k2, whose value is the frequency of the bigram (k1, k2)

sub sequence(@splits){
    my %hash_table;

    



    return %hash_table
}


#part 3:

# Create a function that takes as input a word (and if necessary, your nested hash
# table), and returns a new word.

sub random_word($line){

}