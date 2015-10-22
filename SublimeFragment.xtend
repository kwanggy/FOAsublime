package org.xtext.example.mydsl

import org.eclipse.xtext.xtext.generator.AbstractGeneratorFragment2
import org.eclipse.xtext.GrammarUtil
import java.util.UUID

class SublimeFragment extends AbstractGeneratorFragment2{
	
	override generate() {
                val configFile = '''
                        # [PackageDev] target_format: plist, ext: tmLanguage
                        name: thomas «language.fileExtensions.head»
                        scopeName: source.«language.fileExtensions.head»
                        fileTypes: [«language.fileExtensions.head»]
                        uuid: «UUID.randomUUID»
                        
                        patterns:
                        «collectKeywordsAsRegex»
                        «collectModifierAsRegex»
                        «collectTypeAsRegex»
                '''
                
                projectConfig.genericIdeSrc.generateFile(
                        "thomas.YAML-tmLanguage", configFile)
                
                /* 
                val sublimeConfig = '''
                        # [PackageDev] target_format: plist, ext: tmLanguage
                        name: Sublime Snippet (Raw)
                        scopeName: source.ssraw
                        fileTypes: [ssraw]
                        uuid: 6cbfa751-bc0e-4065-8fe7-38cbad674d9f
                        
                        patterns:
                        - comment: Tab stops like $1, $2...
                          name: keyword.other.ssraw
                          match: «collectKeywordsAsRegEx»
                '''
                */
        }
        
        def collectKeywordsAsRegex() {
                val g = getGrammar
                val keywords = GrammarUtil.getAllKeywords(g)
                val test = '''
                	- name: keyword.other.«language.fileExtensions.head»
                	  match: '''
                
                test.concat(keywords.filter[ matches('\\b(?!String)[A-Z]\\w+\\b') ].join(
                        '\\b(', //before
                        '|', //separator
                        ')\\b' //after
                ) [it].toString)
                
                
                
        }
        def collectModifierAsRegex() {
                val g = getGrammar
                val keywords = GrammarUtil.getAllKeywords(g)
                val test = '''
                	- name: storage.modifier.«language.fileExtensions.head»
                	  match: '''
                
                test.concat(keywords.filter[ matches('\\b(?!int|double|float)[a-z]\\w+\\b') ].join(
                        '\\b(', //before
                        '|', //separator
                        ')\\b' //after
                ) [it].toString)
               
                }
        
        def collectTypeAsRegex() {
                val g = getGrammar
                val keywords = GrammarUtil.getAllKeywords(g)
                val test = '''
                	- name: storage.type.«language.fileExtensions.head»
                	  match: '''
                
                test.concat(keywords.filter[ matches('\\b(int|String|double|float)\\b') ].join(
                        '\\b(', //before
                        '|', //separator
                        ')\\b' //after
                ) [it].toString)
                
                }
	
}