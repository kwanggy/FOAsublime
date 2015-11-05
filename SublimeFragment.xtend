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
                '''
                
                projectConfig.genericIdeSrc.generateFile(
                        "thomas.YAML-tmLanguage", configFile)
                
        }
        
        def collectKeywordsAsRegex() {
                val g = getGrammar
                val keywords = GrammarUtil.getAllKeywords(g)
                val test = '''
                	- name: keyword.other.«language.fileExtensions.head»
                	  match: '''
                
                test.concat(keywords.filter[ matches('\\b(\\w+\\b') ].join(
                        '\\b(', //before
                        '|', //separator
                        ')\\b' //after
                ) [it].toString)
                
                
                
        }
        
	
}