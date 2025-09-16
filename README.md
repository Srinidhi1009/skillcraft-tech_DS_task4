# skillcraft-tech_DS_task4
Traffic Accident Analysis  Analyze traffic accident data to identify patterns related to road conditions, weather, and time of day. Visualize accident hotspots using geographic coordinates and explore contributing factors to improve road safety.

# **Traffic Accident Analysis**

## **Project Overview**

Traffic accidents are a major public safety concern worldwide. This project focuses on analyzing accident patterns related to **road conditions**, **weather**, and **time of day**, and visualizing **accident hotspots**. The visualizations help identify high-risk scenarios, enabling city planners and transportation authorities to implement targeted safety measures.

**Key Objectives:**

* Identify patterns in accident severity based on environmental factors.
* Explore temporal trends in accident frequency.
* Visualize accident hotspots geographically.
* Analyze contributing factors to improve road safety.

## **Visualizations**

### **1. Accidents by Road Condition and Severity**

A **count plot** showing accidents under different road conditions, categorized by severity.

* **Insights:** Wet or icy roads are more prone to severe accidents. Dry roads mostly see minor incidents.

![image alt](https://github.com/Srinidhi1009/skillcraft-tech_DS_task4/blob/f259a7f7b99be78fc66aea30d6ffd26e41b13bd5/Screenshot%202025-09-16%20130413.png)

---

### **2. Accidents by Weather Conditions**

A **bar chart** depicting accident counts by weather type, split by severity.

* **Insights:** Rain, snow, and fog significantly increase the likelihood of severe accidents.

![image alt](https://github.com/Srinidhi1009/skillcraft-tech_DS_task4/blob/1e8fc08192e95a1f3bcffc4a621a1fb343e0e167/Screenshot%202025-09-16%20130447.png)

---

### **3. Accidents by Time of Day**

A **histogram or count plot** showing accident frequency across hours of the day.

* **Insights:** Peak accident times often coincide with morning and evening rush hours.

![image alt](https://github.com/Srinidhi1009/skillcraft-tech_DS_task4/blob/1e8fc08192e95a1f3bcffc4a621a1fb343e0e167/Screenshot%202025-09-16%20130519.png)

---

### **4. Accident Hotspots**

A **scatter plot** visualizing accident locations using latitude and longitude.

* **Insights:** Geographic clusters indicate high-risk areas.
* Optional: Interactive maps can be created using **Folium** for real-time analysis.

![image alt](https://github.com/Srinidhi1009/skillcraft-tech_DS_task4/blob/1e8fc08192e95a1f3bcffc4a621a1fb343e0e167/Screenshot%202025-09-16%20130551.png)

---

### **5. Combined Contributing Factors**

Analyzing **road conditions, weather, and time of day together** can reveal scenarios with the highest risk of severe accidents.

* Example: Wet roads at night lead to a higher proportion of severe incidents.

![image alt](https://github.com/Srinidhi1009/skillcraft-tech_DS_task4/blob/1e8fc08192e95a1f3bcffc4a621a1fb343e0e167/Screenshot%202025-09-16%20130623.png)

---

## **Installation**

1. Ensure Python 3.x is installed.
2. Install required libraries:
3. ```bash
pip install pandas matplotlib seaborn folium

## **Usage**

1. Prepare your accident dataset (`accidents.csv`).
2. Run the analysis script:
3. Outputs:

   * Visualizations of accidents by road condition, weather, and time.
   * Scatter plot of accident hotspots.
   * Insights for high-risk conditions and areas.

## **Project Enhancements**

* **Interactive Maps:** Use Folium for dynamic, zoomable accident hotspot maps.
* **Predictive Modeling:** Apply machine learning to predict accident severity or high-risk locations.
* **Temporal Trends:** Examine monthly, weekly, and seasonal accident patterns.
* **Integration:** Combine accident data with traffic volume, road infrastructure, and population density for deeper insights.

