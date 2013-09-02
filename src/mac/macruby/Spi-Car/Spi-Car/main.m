//
//  main.m
//  Spi-Car
//
//  Created by Aaron Lerch on 9/2/13.
//  Copyright (c) 2013 Aaron Lerch. All rights reserved.
//

#import <Cocoa/Cocoa.h>

#import <MacRuby/MacRuby.h>

int main(int argc, char *argv[])
{
    return macruby_main("rb_main.rb", argc, argv);
}
