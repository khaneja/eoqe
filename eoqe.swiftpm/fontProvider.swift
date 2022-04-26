//
//  File.swift
//  eoqe
//
//  Created by Keshav Khaneja on 4/7/22.
//

import Foundation
import SwiftUI

private let isMainFontRegistered: Bool = false

var cmuSerif: String {
       if !isMainFontRegistered {
           let fontFileName = "CMUSerif-Roman"
           guard let url = Bundle.main.url(forResource: "CMUSerif-Roman", withExtension: "ttf") else {
               fatalError("Unable to find font file \(fontFileName)")
           }
           CTFontManagerRegisterFontsForURL(url as CFURL, CTFontManagerScope.process, nil)
       }
       return "CMUSerif-Roman"
   }

var cmuSerifBold: String {
       if !isMainFontRegistered {
           let fontFileName = "CMUSerif-Bold"
           guard let url = Bundle.main.url(forResource: "CMUSerif-Bold", withExtension: "ttf") else {
               fatalError("Unable to find font file \(fontFileName)")
           }
           CTFontManagerRegisterFontsForURL(url as CFURL, CTFontManagerScope.process, nil)
       }
       return "CMUSerif-Bold"
   }
