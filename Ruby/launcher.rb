#!/usr/bin/env ruby

#Example application to demonstrate some basic Ruby features
#This code loads a given file into an associated application

class Launcher
    # initialize the Laucher class with a map
    # linking applications to files
    def initialize(app_map)
        @app_map = app_map
    end

    # execute the given file using the assotiate app
    def run(file_name)
        application = select_app(file_name)
        system "#{application} #{file_name}"
    end

    # given a file, look up the matching application
    def select_app(file_name)
        ftype = file_type(file_name)
        @app_map[ ftype ]
    end

    # return the part of the file name string after the last '.'
    def file_type(file_name)
        File.exname( file_name ).gsub( /^\./, '').downcase
    end

end

laucher = Launcher.new
